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
	<p><b><a href="${tg.paginate.get_href(1)}" py:content="'&laquo;'" />&nbsp;<a py:strip="tg.paginate.current_page == 1"
	href="${tg.paginate.get_href(tg.paginate.current_page-1)}" py:content="'&larr;'" /></b>&nbsp;
		<b py:for="page in tg.paginate.pages">
	    <a py:strip="page == tg.paginate.current_page"
	        href="${tg.paginate.get_href(page)}" py:content="page"/></b><b>&nbsp;<a py:strip="tg.paginate.current_page == tg.paginate.page_count"
			href="${tg.paginate.get_href(tg.paginate.current_page+1)}" py:content="'&rarr;'" />&nbsp;<a href="${tg.paginate.get_href(tg.paginate.page_count)}" py:content="'&raquo;'" /></b></p>
	<ul>
		<span py:for="course in courses">
			<li><a href="${tg.url('/course/' + str(course.id))}" py:content="course.dept+' '+course.num+': '+course.name">Class</a></li>
		</span>
	</ul>
	<p><b><a href="${tg.paginate.get_href(1)}" py:content="'&laquo;'" />&nbsp;<a py:strip="tg.paginate.current_page == 1"
	href="${tg.paginate.get_href(tg.paginate.current_page-1)}" py:content="'&larr;'" /></b>&nbsp;
		<b py:for="page in tg.paginate.pages">
	    <a py:strip="page == tg.paginate.current_page"
	        href="${tg.paginate.get_href(page)}" py:content="page"/></b><b>&nbsp;<a py:strip="tg.paginate.current_page == tg.paginate.page_count"
			href="${tg.paginate.get_href(tg.paginate.current_page+1)}" py:content="'&rarr;'" />&nbsp;<a href="${tg.paginate.get_href(tg.paginate.page_count)}" py:content="'&raquo;'" /></b></p>
</div>

</body>
</html>
