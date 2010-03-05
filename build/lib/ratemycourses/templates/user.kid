<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>RateMyCourses: <span py:replace="name">NAME</span></title>
</head>
<body>

<div>

	<!-- return dict(dept=dept, num=num, name=name, description=description, instructor_comments=instructor_comments) -->


	<h1><span py:replace="name">User</span></h1>
	<hr />
	<p><b>About ${name}:</b><br />
	${aboutMe}</p>
	<p><b>${name}'s Locker:</b><br />
	<ul>
		<li py:for="i in locker">
			<a href="${tg.url('/course/' + str(i.id))}" py:content="i.dept+' '+i.num+': '+i.name">Page Name Here.</a>
		</li>
	</ul>
	</p>
	<p><b>${name}'s Reviews:</b></p>
	<hr />
	<span py:for="i in range(0,len(reviews))">
		<p><b><a href="${tg.url('/course/' + str(reviews[i].course.id))}">${reviews[i].course.dept+' '+reviews[i].course.num+': '+reviews[i].course.name}</a></b></p>
		<p>Rating: <span py:for="j in range(0,reviews[i].score)"><img src="/static/images/star.jpg" /></span><span py:for="j in range(0,5-reviews[i].score)"><img src="/static/images/nostar.jpg" /></span></p>
		<p>The reviewer took the course with <span py:replace="reviews[i].professor">None</span>.</p>
		<p>Review by: <a href="${tg.url('/user/' + str(reviews[i].reviewer.id))}" py:content="reviews[i].reviewer.display_name">User</a></p>
		<p><span py:replace="reviews[i].contents">Review goes here</span></p>
		<p><i><span py:replace="reviews[i].num_liked">0</span> out of <span py:replace="reviews[i].num_rated">0</span> found this review useful</i></p>
		<hr />
	</span>

</div>

</body>
</html>
