import turbogears as tg
from turbogears import controllers, expose, flash, widgets, validators, validate, error_handler, paginate
from turbogears.toolbox.catwalk import CatWalk
from ratemycourses.model import *
import model
from turbogears import identity, redirect, visit
from cherrypy import request, response, session
from cherrypy.lib import httptools
import time
from turbogears.widgets import AutoCompleteField
import tw.forms as twf
import tw.rating as twr
import tw.extjs as twe
from formencode.schema import Schema
import types, math
from sqlobject import LIKE, func, AND
import md5
import cherrypy
import operator
import simplejson
# from ratemycourses import json
import logging
log = logging.getLogger("ratemycourses.controllers")
class TGSchema(Schema):
	filter_extra_fields = True
	allow_extra_fields = True

class Root(controllers.RootController):
	
	catwalk = CatWalk(model)
	catwalk = identity.SecureObject(catwalk,identity.in_group('admin'))
	
	@expose(template="ratemycourses.templates.login")
	def login(self, forward_url=None, *args, **kw):
		user = request.headers.get("X-Forwarded-User", None)
		visit_key = visit.current().key
		
		identity.current_provider.validate_identity(user, "password", visit_key)
		
		f = Flash2()
		f.ok('You are now logged in as %s!' % user, hideable=True)
		
		if not forward_url:
			forward_url = request.path_info
		if not forward_url or forward_url == '/login' or forward_url == tg.url('/login'):
			forward_url = request.headers.get("Referer", "/")
		if 'cosign' in forward_url:
			redirect('/')
		redirect(tg.url(forward_url, kw))
	
	def makeCloud(self, steps, input):
		if not type(input) == types.ListType or len(input) <= 0 or steps <= 0:
			raise InvalidInputException,\
				  "Please be sure steps > 0 and your input list is not empty."
		else:
			temp, newThresholds, results = [], [], []
			for item in input:
				if not type(item) == types.TupleType:
					raise InvalidInputException, "Be sure input list holds tuples."
				else: temp.append(item[1])
			maxWeight = float(max(temp))
			minWeight = float(min(temp))
			newDelta = (maxWeight - minWeight)/float(steps)
			for i in range(steps + 1):
			   newThresholds.append((100 * math.log((minWeight + i * newDelta) + 2), i))
			for tag in input:
				fontSet = False
				for threshold in newThresholds[1:int(steps)+1]:
					if (100 * math.log(tag[1] + 2)) <= threshold[0] and not fontSet:
						results.append([str(tag[0]),str(threshold[1])])
						fontSet = True
			return results

	@expose("ratemycourses.templates.index")
	def index(self):
		topcourses = list(Course.select(orderBy='viewcount desc'))[0:5]
		#TODO: select only user-generated tags
		tags = Tag.select(orderBy='name')
		catTag = [(tag.name, len(tag.courses)) for tag in tags]
		tagcloud = self.makeCloud(5, catTag)
		fontSizes = { '1':'12px', '2':'14px', '3':'16px', '4':'20px', '5':'24px' }
		return dict(topcourses=topcourses, tagcloud=tagcloud, fontSizes=fontSizes)
	
	@expose()
	def get_course_list(self, node):
		treelist = []
		if node == 'root':
			depts = sorted(list(set([eachclass.dept for eachclass in Course.select()])))
			deptlist = []
			for dept in depts:
				db_dept = Department.select(Department.q.abbr == dept)[0]
				deptlist.append({'text':db_dept.name, 'id':dept})
			deptlist = sorted(deptlist, key=lambda c: c['text'])
			for dept in deptlist:
				treelist.append({	'text':dept['text'],
										'id':dept['id'],
										'cls':'folder',
										'singleClickExpand':'true'})
		else:
			courses = Course.select(Course.q.dept==node)
			courses = sorted(list(courses), key=lambda c:c.num[-1:])
			courses = sorted(courses, key=lambda c:int(c.num[:-1]))
			for course in courses:
				treelist.append({	'text':'%s %s: %s' % (course.dept, course.num, course.name),
										'id':course.id,
										'href':tg.url('course/%d' % course.id),
										'leaf':'true',
										'cls':'file'})
		return simplejson.dumps(treelist)
	
	courseTree = twe.TreeView(divID='treeView1', fetch='/get_course_list', rootID='root', rootText='Courses', title='', collapsible=False, enableDD=False, frame=False)
	
	@expose("ratemycourses.templates.courses")
	def courses(self):
		return dict(courseTree=self.courseTree)
	
	@expose("ratemycourses.templates.tags")
	def tags(self, order="name"):
		tags = list(Tag.select(orderBy='name'))
		if order == 'popularity':
			tags = sorted(tags, key=operator.attrgetter('count'), reverse=True)
		return dict(tags=tags)
	
	@expose("ratemycourses.templates.search")
	def search(self, search, **kw):
		if search == 'Search...' or search == '' or len(search) < 3:
			f = Flash2()
			f.error('You must enter a search term of at least 3 characters',hideable=True)
			redirect(request.headers.get("Referer", "/"))
		courses = list(Course.select(LIKE(Course.q.name,'%'+search+'%')))
		courses.extend(list(Course.select(LIKE(Course.q.description,'%'+search+'%'))))
		tags = Tag.select(LIKE(Tag.q.name,'%'+search+'%'))
		users = User.select(LIKE(User.q.display_name,'%'+search+'%'))
		return dict(courses=courses, tags=tags, users=users, search=search)
	
	@expose("ratemycourses.templates.advsearch")
	def advsearch(self, searchtags=[], submit=""):
		if type(searchtags).__name__ != 'list':
			searchtags = [searchtags]
		tags = Tag.select(orderBy='name')
		results = []
		if searchtags != []:
			results = filter(lambda x: set(searchtags) <= set([t.name for t in x.tags]), Course.select())
		return dict(tags=tags, results=results)

	@identity.require(identity.not_anonymous())
	@expose("ratemycourses.templates.locker")
	def locker(self):
		thisUser = identity.current.user
		locker = thisUser.locker
		return dict(user=thisUser, locker=locker)

	def printRatingStars(self, stars):
		returnString = ''
		originalValue = math.ceil(stars)
		while stars >= 1.0:
			returnString = returnString+'&nbsp;<img src="/static/images/star.png" />'
			stars -= 1.0
		if stars >= 0.4:
			returnString = returnString+'&nbsp;<img src="/static/images/halfstar.png" />'
		for i in range(0,5.0-originalValue):
			returnString = returnString+'&nbsp;<img src="/static/images/nostar.png" />'
		return returnString
	
	@identity.require(identity.not_anonymous())
	@expose()
	def addrating(self, course, **kw):
		print kw
		f = Flash2()
		reviews = list(Course.select(Course.q.id==int(course))[0].reviews)
		totalscore = 0
		for review in reviews:
			totalscore += review.score
		try:
			avgscore = float(totalscore) / len(reviews)
		except ZeroDivisionError:
			avgscore = 'Not rated'
		response = {}
		response['total'] = len(reviews)
		response['average'] = avgscore
		response['message'] = 'Thanks!'
		checkreview = list(Review.select(AND(Review.q.reviewer == identity.current.user, Review.q.course == Course.select(Course.q.id==int(course))[0])))
		if len(checkreview) > 0:
			f.error('Course already rated')
			return simplejson.dumps(response)
		review = Review(score=int(kw['rating']), course = Course.select(Course.q.id==course)[0], reviewer = identity.current.user)
		f.ok('Rating added')
		return simplejson.dumps(response)
	
	@expose("ratemycourses.templates.classpage")
	def course(self, classid):
		thisClass = Course.select(Course.q.id==classid)
		thisClass[0].viewcount += 1
		dept = thisClass[0].dept
		num = thisClass[0].num
		name = thisClass[0].name
		description = thisClass[0].description
		instructor_comments = thisClass[0].instructor_comments
		reviews = thisClass[0].reviews
		tags = sorted([tag for tag in thisClass[0].tags if tag.category == 'user'], key=operator.attrgetter('name'))
		sysTags = sorted([tag for tag in thisClass[0].tags if tag.category != 'user'], key=operator.attrgetter('name'))
		reviewtotal = 0
		for i in range(0,len(reviews)):
			reviewtotal += reviews[i].score
		try:
			avg_score = float(reviewtotal) / len(reviews)
			avg_score = self.printRatingStars(avg_score)
		except ZeroDivisionError:
			avg_score = "Class not rated yet"
		alltags=list(Tag.select(orderBy='name'))
		for tag in set(tags):
			alltags.remove(tag)
		for i in range(0,len(alltags)):
			alltags[i] = alltags[i].name
		relatedCourses = set()
		for review in reviews:
			temp = review.reviewer.reviews
			for i in temp:
				relatedCourses.add(i.course)
		relatedCourses = list(relatedCourses)
		try:
			relatedCourses.remove(thisClass[0])
		except ValueError:
			True
		ratingWidget = twr.Rating(action='/addrating?course=%s' % classid, label_text='Add a rating:', id='rating', on_click='window.location.reload();')
		crosslinks = []
		for cl in thisClass[0].crosslinks:
			otherclass = [c for c in cl.courses if c.id != int(classid)][0]
			crosslinks.append({'otherclass':otherclass, 'description':cl.description})
		return dict(classid=classid, dept=dept, num=num, name=name, description=description, instructor_comments=instructor_comments, reviews=reviews, tags=tags,
						sysTags=sysTags, avg_score=avg_score, alltags=alltags, relatedCourses=relatedCourses[0:5], ratingWidget=ratingWidget, crosslinks=crosslinks)

	@expose("ratemycourses.templates.user")
	def user(self, userid):
		thisUser = User.select(User.q.id==userid)
		alias = thisUser[0].display_name
		reviews = thisUser[0].reviews
		aboutMe = thisUser[0].about_me
		locker = thisUser[0].locker
		return dict(name=alias, reviews=reviews, aboutMe=aboutMe, locker=locker)

	@expose("ratemycourses.templates.tag")
	@paginate('courses', limit=25, max_pages=10)
	def tag(self, tagName):
		thisTag = Tag.byName(tagName)
		courses = thisTag.courses
		description = thisTag.description
		if not description:
		    description = "This tag does not yet have a description.";
		return dict(name=tagName, courses=courses, description=description)
		
	@expose("ratemycourses.templates.edittag")
	def edittag(self, tagName):
		thisTag = Tag.byName(tagName)
		description = thisTag.description
		if not description:
		    description = "This tag does not yet have a description.";
		return dict(tagName=tagName, description=description)
		
	@expose()
	def savetag(self, tagName, data, submit):
		thisTag = Tag.byName(tagName)
		thisTag.description = data
		#TODO: flash success
		raise redirect("/tag", tagName=tagName)

	addreview_form = twf.TableForm('addreview_form', action='/savereview', show_errors=True, validator=TGSchema, children=[
		twf.HiddenField('classid', validator=twf.validators.Int(not_empty=True)),
		twf.SingleSelectField('rating', options=['', '1', '2', '3', '4', '5'], validator=twf.validators.Int(not_empty=True)),
		twf.TextField('professor', validator=twf.validators.UnicodeString(not_empty=True)),
		twf.TextArea('review', validator=twf.validators.UnicodeString(not_empty=True))
	])

	@identity.require(identity.not_anonymous())
	@expose("ratemycourses.templates.addreview")
	def addreview(self, classid):
		thisClass = Course.select(Course.q.id==classid)
		dept = thisClass[0].dept
		num = thisClass[0].num
		name = thisClass[0].name
		return dict(form=self.addreview_form, formclassid=dict(classid=classid), dept=dept, num=num, name=name)

	@identity.require(identity.not_anonymous())
	@expose("ratemycourses.templates.editprofile")
	def editprofile(self):
		thisUser = identity.current.user
		return dict(alias=thisUser.display_name, username=thisUser.user_name, aboutMe=thisUser.about_me)

	@identity.require(identity.not_anonymous())
	@expose()
	def saveprofile(self, alias, aboutMe, submit):
		thisUser = identity.current.user
		thisUser.display_name = alias
		thisUser.about_me = aboutMe
		f = Flash2()
		f.ok("Profile Updated!", hideable=True)
		raise redirect('/')

	@validate(form=addreview_form)
	@error_handler(addreview)
	@identity.require(identity.not_anonymous())
	@expose()
	def savereview(self, classid, rating, review, professor):
		thisClass = Course.select(Course.q.id==classid)
		review = Review(score=int(rating), num_liked=0, num_rated=0, professor=professor, contents=review, reviewer=identity.current.user, course=thisClass[0])
		f = Flash2()
		f.ok("Review Added!", hideable=True)
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)
	
	@identity.require(identity.not_anonymous())
	@expose()
	def addtolocker(self, classid):
		f = Flash2()
		thisClass = Course.select(Course.q.id==classid)[0]
		thisUser = identity.current.user
		try:
			thisUser.locker.index(thisClass)
			f.warning(thisClass.dept+" "+thisClass.num+": "+thisClass.name+" Was Already In Your Locker.", hideable=True)
		except ValueError:
			thisUser.addCourse(thisClass)
			f.ok(thisClass.dept+" "+thisClass.num+": "+thisClass.name+" Has Been Added to Your Locker!", hideable=True)
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)
	
	@identity.require(identity.not_anonymous())
	@expose()
	def clearlocker(self):
		thisUser = identity.current.user
		for i in set(thisUser.locker):
			thisUser.removeCourse(i)
		raise redirect('/locker')

	@identity.require(identity.not_anonymous())
	@expose()
	def flagreview(self, reviewid, classid):
		thisReview = Review.select(Review.q.id==reviewid)[0]
		thisReview.flagged += 1
		f = Flash2()
		f.info("Rating flagged", hideable=True)
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)
	
	@identity.require(identity.not_anonymous())
	@expose()
	def likedreview(self, reviewid, classid):
		thisReview = Review.select(Review.q.id==reviewid)[0]
		thisReview.num_liked += 1
		thisReview.num_rated += 1
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)

	@identity.require(identity.not_anonymous())
	@expose()
	def dislikedreview(self, reviewid, classid):
		thisReview = Review.select(Review.q.id==reviewid)[0]
		thisReview.num_rated += 1
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)
	
	acfield = AutoCompleteField(	search_controller = "/searchtag",
											search_param = "input",
											result_name = "matches",
											name= "tag")
	
	@expose("ratemycourses.templates.addtag")
	def addtag(self, classid):
		course = Course.select(Course.q.id==classid)[0]
		tags = Tag.select(orderBy='name')
		return dict(course=course, acfield=self.acfield, tags=tags)
	
	@expose("ratemycourses.templates.addcrosslink")
	def addcrosslink(self, classid):
		course = Course.select(Course.q.id==classid)[0]
		courses = Course.select()
		courses = sorted(list(courses), key=lambda c:c.num[-1:])
		courses = sorted(courses, key=lambda c:int(c.num[:-1]))
		courses = sorted(courses, key=lambda c:c.dept)		
		return dict(course=course, all_courses=courses)
	
	@identity.require(identity.not_anonymous())
	@expose()
	def crosslinkcourse(self, course1, course2, description):
		crosslink = CrossLink(description=description, creator=identity.current.user)
		course1obj = Course.select(Course.q.id==course1)[0]
		crosslink.addCourse(course1obj)
		course2obj = Course.select(Course.q.id==course2)[0]
		crosslink.addCourse(course2obj)
		f = Flash2()
		f.ok('CrossLink between %s %s and %s %s added' % (course1obj.dept, course1obj.num, course2obj.dept, course2obj.num), hideable=True)
		return '<html><body><script type="text/javascript">self.parent.location.reload(true);</script></html>'
	
	@expose(format = "json")
	def searchtag(self, input):
		input = input.lower()
		matches = list(Tag.select(LIKE(func.lower(Tag.q.name),input+"%"), orderBy=Tag.q.name))
		matches = [tag.name for tag in matches]
		return dict(matches=matches)
	
	@identity.require(identity.not_anonymous())
	@expose()
	def tagcourse(self, **kw):
		tag = kw['tag']['text']
		classid = kw['courseid']
		thisCourse = Course.select(Course.q.id==classid)
		f = Flash2()
		if tag == 'null' or tag == 'undefined':
			f.error('You must enter a tag')
			return '<html><body><script type="text/javascript">self.parent.location.reload(true);</script></html>'
		try:
			Tag.byName(tag)
		except SQLObjectNotFound:
			tag = tag.replace(' ','')
			if len(tag) > 1:
				tag = tag[0].upper()+tag[1:]
			temp = Tag(name=tag)
		if Tag.byName(tag) in thisCourse[0].tags:
			f.error('Tag already exists')
			return '<html><body><script type="text/javascript">self.parent.location.reload(true);</script></html>'
		thisCourse[0].addTag(Tag.byName(tag))
		f.ok("Tag "+tag+" Added", hideable=True)
		return '<html><body><script type="text/javascript">self.parent.location.reload(true);</script></html>'

	@identity.require(identity.not_anonymous())
	@expose()
	def untagcourse(self, classid, tag):
		thisUser = identity.current.user
		if(thisUser.admin):
			try:
				Tag.byName(tag)
				thisCourse = Course.select(Course.q.id==classid)
				thisCourse[0].removeTag(Tag.byName(tag))
				f = Flash2()
				f.ok("Tag "+tag+" Removed", hideable=True)
			except SQLObjectNotFound:
				True
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)

	@identity.require(identity.not_anonymous())
	@expose()
	def deletereview(self, classid, reviewid):
		thisUser = identity.current.user
		if(thisUser.admin):
			thisReview = Review.select(Review.q.id==reviewid)[0]
			thisReview.destroySelf()
			f = Flash2()
			f.ok("Review deleted", hideable=True)
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)

	@expose()
	def logout(self):
		identity.current.logout()
		redirect("https://login.brandeis.edu/cgi-bin/logout?verify=Logout")

class ReviewFields(widgets.WidgetsList):
	"""The WidgetsList defines the fields of the form."""
	classid = widgets.HiddenField()
	rating = widgets.RadioButtonList(options=[(1,1),(2,2),(3,3),(4,4),(5,5)])
	professor = widgets.TextField(validator=validators.NotEmpty())
	review = widgets.TextArea(validator=validators.NotEmpty())

class Flash2Message:
	def __init__(self, msg, cls='info', html=False, hideable=False):
		self.message = msg
		self.css = cls
		self.html = html
		self.hideable = hideable
		self.md5 = md5.md5(self.message).hexdigest()
	

class Flash2:
	def __init__(self):
		self.messages = []
		self.messages_dict = {'info':[], 'warning':[], 'error':[], 'ok':[]}
		self.generator = self._generator() # use f2.generator.next() to get messages
		self.next = self._generator # next() method to make class iterable
	
	def __iter__(self):
		return self.generator
	
	def add_message(self, msg, cls, html=False, growl=False, hideable=False):
		m = Flash2Message(msg, cls, html, hideable)
		self.messages.append(m)
		if cls not in self.messages_dict:
			self.messages_dict[cls] = []
		self.messages_dict[cls].append(m)
		cherrypy.session['flash2'] = self # stick the generator in the TG/CP session; use it in master template
	
	def _generator(self):
		"""
		Build a generator for getting messages from a Flash2 instance
		"""
		while(1):
			try:
				m = self.messages.pop(0) # pop the first Flash2Message in the list
				yield m
			except IndexError:
				raise StopIteration
	
	def info(self, msg, html=False, hideable=True, growl=False):
		self.add_message(msg, 'info', html, growl, hideable)
	
	def warning(self, msg, html=False, hideable=True, growl=False):
		self.add_message(msg, 'warning', html, growl, hideable)
	
	def error(self, msg, html=False, hideable=True, growl=False):
		self.add_message(msg, 'error', html, growl, hideable)
	
	def ok(self, msg, html=False, hideable=True, growl=False):
		self.add_message(msg, 'ok', html, growl, hideable)
	
