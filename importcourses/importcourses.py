#!/usr/bin/python
import sys
from ratemycourses.model import *
import csv
import progress

courses_file = 'importcourses/infiles/combined.csv'
courses = csv.DictReader(open(courses_file),delimiter='|',quotechar='>')
course_rows = list(courses)

progress_meter = progress.ProgressMeter(total=len(course_rows))

all_courses = []
dupes = []
current_course = None

# Some colors
RED = '\033[91m'
BLUE = '\033[94m'
ENDC = '\033[0m'

# Tag mappings
tag_maps = {'CA':'CreativeArts',
				'FL':'ForeignLanguage',
				'HUM':'Humanities',
				'NW':'NonWestern',
				'OC':'OralCommunication',
				'PE-1':'PhysicalEducation',
				'PE-SC':'PhysicalEducation',
				'QR':'QuantitativeReasoning',
				'QR1':'QuantitativeReasoningLecture',
				'QR2':'QuantitativeReasoningLab',
				'SN':'ScienceReq',
				'SS':'SocialScienceReq',
				'USEM':'USEM',
				'USWI':'USEMPlusW',
				'UWS':'UWS',
				'WI':'WritingIntensive'}

for row in course_rows:
	progress_meter.update(1)
	row['num'] = row['num'].strip()
	row['desc'] = row['desc'].replace("\\n",'\n').replace('\\"','"')
	row['name'] = row['name'].replace('\\"','"')
	row['req'] = row['req'].replace('\\N','')
	if not current_course or not (row['dept'] == current_course['dept'] and row['num'] == current_course['num']):
		if current_course:
			all_courses.append(current_course)
		current_course = row
		continue
	if not current_course['desc'] == row['desc']:
		current_course['desc'] = row['desc']
	if not current_course['name'] == row['name']:
		current_course['name'] = row['name']
	if not row['req'] in current_course['req']:
		current_course['req'] = current_course['req']+' '+row['req']
all_courses.append(current_course)

#for course in all_courses:
#	print("%sCourse:%s %s %s\n%sDesc:%s\n%s\n%sReqs:%s %s\n\n" %
#		(RED,ENDC,course['dept'], course['num'], BLUE,ENDC,course['desc'], BLUE,ENDC,course['req']))
#print len(all_courses)

old_courses = 0
new_courses = 0

for this_course in all_courses:
	db_course = Course.selectBy(dept=this_course['dept'],num=this_course['num'])
	if db_course.count() > 0:
		db_course = db_course[0]
		db_course.name = this_course['name']
		db_course.description = this_course['desc']
		for tag in this_course['req'].split():
			add_tag = Tag.byName(tag_maps[tag])
			if not add_tag in db_course.tags:
				db_course.addTag(add_tag)
		old_courses += 1
	else:
		db_course = Course(dept=this_course['dept'], num=this_course['num'], name=this_course['name'], description=this_course['desc'])
		for tag in this_course['req'].split():
			add_tag = Tag.byName(tag_maps[tag])
			db_course.addTag(add_tag)
		new_courses += 1

print "New courses: %d\nUpdated courses: %d\n" % (new_courses,old_courses)

