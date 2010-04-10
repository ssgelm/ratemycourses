<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>Welcome to RateMyCourses</title>
</head>
<body>

<div style="float: left; width: 30%; text-align: center;" class="orientation">
<div class="question">New to RateMyCourses?</div>
<a class="answer" href="${tg.url('/login')}">Yes, get me started!</a>
<a class="answer" href="${tg.url('/login')}">I've been here before, log me in!</a>
<a class="answer" href="#">Just browsing, thanks.</a>
</div>

<div style="float: right; width: 65%; margin-bottom: 10px; padding: 5px; text-align: justify;">
    
	<p>Welcome to RateMyCourse. The aim of this website is to build relationships between courses across the bulletin by tagging classes with keywords, while also providing the ability to add course ratings.</p>

    <p>To get started, click the "Courses" tab on the top menu to browse by departments or the "Tags" tab to see requirements and keywords associated with classes.</p>

</div>

<div style="clear: both; margin-top: 10px; padding: 5px;">
	<p style="line-height: 250%;" align="justify"><b>Popular Tags:</b><br /><span py:for="tag in tagcloud"><a class="tag" href="${tg.url('/tag/'+tag[0])}" style="font-size:${fontSizes[tag[1]]}" py:content="tag[0]">Tag</a> </span></p>

	<!--<p><b>Most Viewed Courses:</b>
	<ul>
		<li py:for="course in topcourses">
			<a href="${tg.url('/course/' + str(course.id))}" py:content="course.dept+' '+course.num+': '+course.name">Page Name Here.</a>
		</li>
	</ul></p>-->

</div>

</body>
</html>
