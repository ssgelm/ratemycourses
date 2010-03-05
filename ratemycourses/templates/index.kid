<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>Welcome to RateMyCourses</title>
</head>
<body>

<div>
    
	<p>Welcome to RateMyCourses, a new approach to the Brandeis course database. The aim of this website is to build relationships between courses across the bulletin by tagging classes with keywords, while also allowing for personal comments and course ratings.</p>

	<p>To get started, click the "Courses" link on the left-hand side to browse by departments or the "Tags" link to see requirements and keywords associated with classes.</p>

	<p>Also, feel free to browse by the most popular tags and courses below. In the "Tag Cloud," the larger the tag is the more classes are tagged with it.</p>

	<p>To leave a review you must login using your Brandeis UNET ID and password.</p>

	<p align="justify"><b>Tag Cloud:</b><br /><span py:for="tag in tagcloud"><a href="${tg.url('/tag/'+tag[0])}" style="font-size:${fontSizes[tag[1]]}" py:content="tag[0]">Tag</a> </span></p>

	<p><b>Most Viewed Courses:</b>
	<ul>
		<li py:for="course in topcourses">
			<a href="${tg.url('/course/' + str(course.id))}" py:content="course.dept+' '+course.num+': '+course.name">Page Name Here.</a>
		</li>
	</ul></p>

</div>

</body>
</html>
