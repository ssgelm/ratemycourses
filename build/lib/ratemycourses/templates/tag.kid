<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>RateMyCourses: <span py:replace="name">TAG</span></title>
</head>
<body>

<div>

	<h1><span py:replace="name">Tag</span></h1>
	<hr />
	<p><b>Courses tagged with <span py:replace="name">Tag</span>:</b></p>
	<ul>
		<span py:for="i in range(0,len(courses))">
			<li><a href="${tg.url('/course/' + str(courses[i].id))}" py:content="str(courses[i].dept+' '+courses[i].num+': '+courses[i].name)">Class</a></li>
		</span>
	</ul>
</div>

</body>
</html>
