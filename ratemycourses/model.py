from datetime import datetime
import pkg_resources
pkg_resources.require("SQLObject>=0.10.1")
from turbogears.database import PackageHub
# import some basic SQLObject classes for declaring the data model
# (see http://www.sqlobject.org/SQLObject.html#declaring-the-class)
from sqlobject import SQLObject, SQLObjectNotFound, RelatedJoin, MultipleJoin, ForeignKey
# import some datatypes for table columns from SQLObject
# (see http://www.sqlobject.org/SQLObject.html#column-types for more)
from sqlobject import StringCol, UnicodeCol, IntCol, DateTimeCol, BoolCol
from turbogears import identity

__connection__ = hub = PackageHub('ratemycourses')


# your data model


# class YourDataClass(SQLObject):
#	 pass

# Tag: id, name
class Tag(SQLObject):
	name = UnicodeCol(alternateID = True, length = 255)
	created = DateTimeCol(default=datetime.now)
	courses = RelatedJoin('Course', orderBy=['dept', 'num'])
	
	def _get_count(self):
		return len(self.courses)
	count = property(_get_count)
	description = UnicodeCol(default='')
	category = UnicodeCol(default='user') # enumerate('userDefined', 'department', 'majorReq', ...) would be better

# Review: id, score, num_liked, num_rated, professor, reviewer
class Review(SQLObject):
	score = IntCol()
	num_liked = IntCol()
	num_rated = IntCol()
	professor = UnicodeCol(length = 255)
	contents = UnicodeCol()
	created = DateTimeCol(default=datetime.now)
	reviewer = ForeignKey('User')
	course = ForeignKey('Course')
	flagged = IntCol(default=0)

# Course: id, name, description, instructor_comments, avg_score
class Course(SQLObject):
	dept = UnicodeCol(length = 255)
	num = UnicodeCol(length = 255)
	name = UnicodeCol(length = 255)
	description = UnicodeCol()
	instructor_comments = UnicodeCol(default='')
	created = DateTimeCol(default=datetime.now)
	reviews = MultipleJoin('Review')
	tags = RelatedJoin('Tag')
	in_locker = RelatedJoin('User', joinColumn='course_id', otherColumn='tg_user_id', intermediateTable='course_tg_user')
	viewcount = IntCol(default=0)

# Department: id, abbr, name
class Department(SQLObject):
	abbr = UnicodeCol(length = 4)
	name = UnicodeCol(length = 255)

# the identity model


class Visit(SQLObject):
	"""
	A visit to your site
	"""
	class sqlmeta:
		table = 'visit'

	visit_key = StringCol(length=40, alternateID=True,
						  alternateMethodName='by_visit_key')
	created = DateTimeCol(default=datetime.now)
	expiry = DateTimeCol()

	def lookup_visit(cls, visit_key):
		try:
			return cls.by_visit_key(visit_key)
		except SQLObjectNotFound:
			return None
	lookup_visit = classmethod(lookup_visit)


class VisitIdentity(SQLObject):
	"""
	A Visit that is link to a User object
	"""
	visit_key = StringCol(length=40, alternateID=True,
						  alternateMethodName='by_visit_key')
	user_id = IntCol()


class Group(SQLObject):
	"""
	An ultra-simple group definition.
	"""
	# names like "Group", "Order" and "User" are reserved words in SQL
	# so we set the name to something safe for SQL
	class sqlmeta:
		table = 'tg_group'

	group_name = UnicodeCol(length=16, alternateID=True,
							alternateMethodName='by_group_name')
	display_name = UnicodeCol(length=255)
	created = DateTimeCol(default=datetime.now)

	# collection of all users belonging to this group
	users = RelatedJoin('User', intermediateTable='user_group',
						joinColumn='group_id', otherColumn='user_id')

	# collection of all permissions for this group
	permissions = RelatedJoin('Permission', joinColumn='group_id',
							  intermediateTable='group_permission',
							  otherColumn='permission_id')


class User(SQLObject):
	"""
	Reasonably basic User definition.
	Probably would want additional attributes.
	"""
	# names like "Group", "Order" and "User" are reserved words in SQL
	# so we set the name to something safe for SQL
	class sqlmeta:
		table = 'tg_user'

	user_name = UnicodeCol(length=16, alternateID=True,
						   alternateMethodName='by_user_name')
	email_address = UnicodeCol(length=255, alternateID=True,
							   alternateMethodName='by_email_address')
	display_name = UnicodeCol(length=255)
	#password = UnicodeCol(length=40)
	created = DateTimeCol(default=datetime.now)
	
	realname = BoolCol(default=False)
	reviews = MultipleJoin('Review', joinColumn='reviewer_id')

	locker = RelatedJoin('Course', joinColumn='tg_user_id', otherColumn='course_id', intermediateTable='course_tg_user', orderBy=['dept', 'num'])

	admin = BoolCol(default=False)

	about_me = UnicodeCol(default='')
	
	# groups this user belongs to
	groups = RelatedJoin('Group', intermediateTable='user_group',
						 joinColumn='user_id', otherColumn='group_id')

	def _get_permissions(self):
		perms = set()
		for g in self.groups:
			perms |= set(g.permissions)
		return perms

	def _set_password(self, cleartext_password):
		"""Runs cleartext_password through the hash algorithm before saving."""
		password_hash = identity.encrypt_password(cleartext_password)
		self._SO_set_password(password_hash)

	def set_password_raw(self, password):
		"""Saves the password as-is to the database."""
		self._SO_set_password(password)


class Permission(SQLObject):
	"""
	A relationship that determines what each Group can do
	"""
	permission_name = UnicodeCol(length=16, alternateID=True,
								 alternateMethodName='by_permission_name')
	description = UnicodeCol(length=255)

	groups = RelatedJoin('Group',
						 intermediateTable='group_permission',
						 joinColumn='permission_id',
						 otherColumn='group_id')
