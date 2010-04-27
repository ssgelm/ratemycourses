import ldap

import turbogears.config
from turbogears.identity.soprovider import *
from turbogears.database import session
from turbogears import redirect
from cherrypy import request, response
from ratemycourses.model import *
from sqlobject import SQLObjectNotFound

class SoCosignIdentityProvider(SqlObjectIdentityProvider):
	"""
	IdentityProvider that uses Cosign for authentication.
	"""

	def __init__(self):
		super(SoCosignIdentityProvider, self).__init__()
		get = turbogears.config.get

		self.host = get("identity.socosignprovider.host", "localhost")
		self.port = get("identity.socosignprovider.port", 389)
		self.basedn  = get("identity.socosignprovider.basedn", "dc=localhost")
		self.filter_id  = get("identity.socosignprovider.filter_id", "uid")
		self.autocreate = get("identity.socosignprovider.autocreate", False)

		log.info("host :: %s" % self.host)
		log.info("port :: %d" % self.port)
		log.info("basedn :: %s" % self.basedn)
		log.info("autocreate :: %s" % self.autocreate)

	def validate_identity(self, user_name, password, visit_key):
		if request.headers.get("X-Forwarded-User", None) == '(null)':
			redirect("/login")
			return None
		objects = self.validate_password(None, user_name, password)
		if objects:
			try:
				user = User.by_user_name(user_name)
			except SQLObjectNotFound:
				if self.autocreate:
					email_address = user_name+"@brandeis.edu"
					try:
						display_name=objects[0][1]['cn'][2]
					except (IndexError, KeyError):
						try:
							display_name=objects[0][1]['cn'][0]
						except (IndexError, KeyError):
							display_name=user_name
					user = User(user_name=user_name, display_name=display_name, email_address=email_address)
				else:
					return None
			try:
				link = VisitIdentity.by_visit_key(visit_key)
			except SQLObjectNotFound:
				link = VisitIdentity(visit_key=visit_key, user_id=user.id)
			link.user_id = user.id
			return SqlObjectIdentity(visit_key, user)
		return None

	def validate_password( self, user, user_name, password ):
		'''
		Validates user_name and password against an AD domain.
		
		'''
		
		ldapcon = ldap.open(self.host, self.port)
		filter = "(%s=%s)" % (self.filter_id, user_name)
		rc = ldapcon.search(self.basedn, ldap.SCOPE_SUBTREE, filter)
							
		objects = ldapcon.result(rc)[1]
		
		if(len(objects) == 0):
			log.warning("No such LDAP user: %s" % user_name)
			objects = [[]]
		elif(len(objects) > 1):
			log.error("Too many users: %s" % user_name)
		
		loggedinusername = request.headers.get("X-Forwarded-User", None)
		
		if not user_name == loggedinusername:
			return False
		
		return objects
	

