<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>Welcome to RateMyCourses</title>
</head>
<body>

<div>
    
	<h1>Search results for '${search}':</h1>
    
	<h2>Users</h2>
	<ul>
		<li py:for="user in users">
			<a href="${tg.url('/user/' + str(user.id))}" py:content="user.display_name">Page Name Here.</a>
		</li>
	</ul>
	<h2>Tags</h2>
	<ul>
		<li py:for="tag in tags">
			<a href="${tg.url('/tag/' + tag.name)}" py:content="tag.name">Page Name Here.</a>
		</li>
	</ul>
	<h2>Courses</h2>
	<ul>
		<li py:for="course in courses">
			<a href="${tg.url('/course/' + str(course.id))}" py:content="course.dept+' '+course.num+': '+course.name">Page Name Here.</a>
		</li>
	</ul>

</div>

</body>
</html>
