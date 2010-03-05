import turbogears as tg
from turbogears import controllers, expose, flash, widgets, validators, validate, error_handler
from ratemycourses.model import *
from turbogears import identity, redirect
from cherrypy import request, response
import tw.forms as twf
from formencode.schema import Schema
import types, math
from sqlobject import LIKE
# from ratemycourses import json
import logging
log = logging.getLogger("ratemycourses.controllers")
class TGSchema(Schema):
	filter_extra_fields = True
	allow_extra_fields = True

class Root(controllers.RootController):

	@expose(template="ratemycourses.templates.login")
	def login(self, forward_url=None, *args, **kw):

		if forward_url:
			if isinstance(forward_url, list):
				forward_url = forward_url.pop(0)
			else:
				del request.params['forward_url']

		if not identity.current.anonymous and identity.was_login_attempted() \
				and not identity.get_identity_errors():
			redirect(tg.url(forward_url or '/', kw))

		if identity.was_login_attempted():
			msg = _("The credentials you supplied were not correct or "
				   "did not grant access to this resource.")
		elif identity.get_identity_errors():
			msg = _("Please log in using your Brandeis UNET ID and password.")
		else:
			msg = _("Please log in using your Brandeis UNET ID and password.")
			if not forward_url:
				forward_url = request.headers.get("Referer", "/")

		response.status = 401
		return dict(logging_in=True, message=msg,
			forward_url=forward_url, previous_url=request.path_info,
			original_parameters=request.params)

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
		tags = Tag.select(orderBy='name')
		catTag = [(tag.name, len(tag.courses)) for tag in tags]
		tagcloud = self.makeCloud(5, catTag)
		fontSizes = { '1':'12px', '2':'14px', '3':'16px', '4':'20px', '5':'24px' }
		return dict(topcourses=topcourses, tagcloud=tagcloud, fontSizes=fontSizes)

	@expose("ratemycourses.templates.courses")
	def courses(self, subject=None):
		if subject:
			idlist = [eachclass.id for eachclass in Course.select(Course.q.dept==subject)]
			namelist = [eachclass.name for eachclass in Course.select(Course.q.dept==subject)]
			deptlist = [eachclass.dept for eachclass in Course.select(Course.q.dept==subject)]
			numlist = [eachclass.num for eachclass in Course.select(Course.q.dept==subject)]
		else:
			idlist = [eachclass.id for eachclass in Course.select(orderBy='dept')]
			namelist = [eachclass.name for eachclass in Course.select(orderBy='dept')]
			deptlist = [eachclass.dept for eachclass in Course.select(orderBy='dept')]
			numlist = [eachclass.num for eachclass in Course.select(orderBy='dept')]
		depts = sorted(list(set([eachclass.dept for eachclass in Course.select()])))
		return dict(idlist=idlist, namelist=namelist, deptlist=deptlist, numlist=numlist, depts=depts, currentdept=subject)
	
	@expose("ratemycourses.templates.tags")
	def tags(self, order="name"):
		taglist = [eachtag.name for eachtag in Tag.select(orderBy='name')]
		tagcount = [len(eachtag.courses) for eachtag in Tag.select(orderBy='name')]
		tags=[[taglist[i], tagcount[i]] for i in range(0,len(taglist))]
		if order=="popularity":
			tags.sort(lambda x, y: x[1]-y[1])
			tags.reverse()
		return dict(tags=tags)
	
	@expose("ratemycourses.templates.search")
	def search(self, search):
		courses = list(Course.select(LIKE(Course.q.name,'%'+search+'%')))
		courses.extend(list(Course.select(LIKE(Course.q.description,'%'+search+'%'))))
		tags = Tag.select(LIKE(Tag.q.name,'%'+search+'%'))
		users = User.select(LIKE(User.q.display_name,'%'+search+'%'))
		return dict(courses=courses, tags=tags, users=users, search=search)

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
			returnString = returnString+'<img src="/static/images/star.jpg" />'
			stars -= 1.0
		if stars >= 0.4:
			returnString = returnString+'<img src="/static/images/halfstar.jpg" />'
		for i in range(0,5.0-originalValue):
			returnString = returnString+'<img src="/static/images/nostar.jpg" />'
		return returnString

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
		tags = thisClass[0].tags
		reviewtotal = 0
		for i in range(0,len(reviews)):
			reviewtotal += reviews[i].score
		try:
			avg_score = float(reviewtotal) / len(reviews)
			avg_score = self.printRatingStars(avg_score)
		except ZeroDivisionError:
			avg_score = "Class not rated yet"
		alltags=list(Tag.select(orderBy='name'))
		for tag in tags:
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
		return dict(classid=classid, dept=dept, num=num, name=name, description=description, instructor_comments=instructor_comments, reviews=reviews, tags=tags, avg_score=avg_score, alltags=alltags, relatedCourses=relatedCourses[0:5])

	@expose("ratemycourses.templates.user")
	def user(self, userid):
		thisUser = User.select(User.q.id==userid)
		alias = thisUser[0].display_name
		reviews = thisUser[0].reviews
		aboutMe = thisUser[0].about_me
		locker = thisUser[0].locker
		return dict(name=alias, reviews=reviews, aboutMe=aboutMe, locker=locker)

	@expose("ratemycourses.templates.tag")
	def tag(self, tagName):
		thisTag = Tag.byName(tagName)
		courses = thisTag.courses
		return dict(name=tagName, courses=courses)

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

	@expose()
	def saveprofile(self, alias, aboutMe, submit):
		thisUser = identity.current.user
		thisUser.display_name = alias
		thisUser.about_me = aboutMe
		flash("Profile Updated!")
		raise redirect('/')

	@validate(form=addreview_form)
	@error_handler(addreview)
	@expose()
	def savereview(self, classid, rating, review, professor):
		thisClass = Course.select(Course.q.id==classid)
		review = Review(score=int(rating), num_liked=0, num_rated=0, professor=professor, contents=review, reviewer=identity.current.user, course=thisClass[0])
		flash("Review Added!")
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)
	
	@identity.require(identity.not_anonymous())
	@expose()
	def addtolocker(self, classid):
		thisClass = Course.select(Course.q.id==classid)[0]
		thisUser = identity.current.user
		try:
			thisUser.locker.index(thisClass)
			flash(thisClass.dept+" "+thisClass.num+": "+thisClass.name+" Was Already In Your Locker.")
		except ValueError:
			thisUser.addCourse(thisClass)
			flash(thisClass.dept+" "+thisClass.num+": "+thisClass.name+" Has Been Added to Your Locker!")
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
		flash("Rating flagged")
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

	@expose()
	def tagcourse(self, classid, tag='null'):
		thisCourse = Course.select(Course.q.id==classid)
		if tag == 'null' or tag == 'undefined':
			myRedirect = "/course/"+str(classid)
			raise redirect(myRedirect)
		try:
			Tag.byName(tag)
		except SQLObjectNotFound:
			tag = tag.replace(' ','')
			if len(tag) > 1:
				tag = tag[0].upper()+tag[1:]
			temp = Tag(name=tag)
		thisCourse[0].addTag(Tag.byName(tag))
		flash("Tag "+tag+" Added")
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)

	@identity.require(identity.not_anonymous())
	@expose()
	def untagcourse(self, classid, tag):
		thisUser = identity.current.user
		if(thisUser.admin):
			try:
				Tag.byName(tag)
				thisCourse = Course.select(Course.q.id==classid)
				thisCourse[0].removeTag(Tag.byName(tag))
				flash("Tag "+tag+" Removed")
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
			flash("Review deleted")
		myRedirect = "/course/"+str(classid)
		raise redirect(myRedirect)


	@expose()
	def logout(self):
		identity.current.logout()
		redirect("/")

class ReviewFields(widgets.WidgetsList):
	"""The WidgetsList defines the fields of the form."""
	classid = widgets.HiddenField()
	rating = widgets.RadioButtonList(options=[(1,1),(2,2),(3,3),(4,4),(5,5)])
	professor = widgets.TextField(validator=validators.NotEmpty())
	review = widgets.TextArea(validator=validators.NotEmpty())

