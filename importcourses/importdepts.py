#!/usr/bin/python
import sys
import csv

courses_file = 'infiles/depts.csv'
courses = csv.DictReader(open(courses_file),delimiter=',',quotechar='"')
course_rows = list(courses)


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
	if len(row['abbr']) <= 4:
		print 'dept = Department(abbr="%s", name="%s")' % (row['abbr'], row['name'])

