<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>Welcome to RateMyCourses</title>
<script language="javascript">
function nav()
	{
		var w = document.subjectdropdown.subject.selectedIndex;
		var url_add = document.subjectdropdown.subject.options[w].value;
		window.location.href = ${tg.url('/courses/')}+url_add;
	}
</script>
</head>
<body>

<div>
    
	<p>Here are the classes that are currently in the system:</p>
   
	<p><form method="get" action="${tg.url('/courses/')}" name="subjectdropdown">
		<select name="subject" onChange="nav()">
			<option value="">Select a Department</option>
			<option value="">----</option>
			<option value="">All</option>
			<option py:for="dept in depts" py:value="dept" py:content="dept">DEPT</option>
		</select>
	</form></p>
	<p><b><a href="${tg.paginate.get_href(1)}" py:content="'&laquo;'" />&nbsp;<a py:strip="tg.paginate.current_page == 1"
	href="${tg.paginate.get_href(tg.paginate.current_page-1)}" py:content="'&larr;'" /></b>&nbsp;
		<b py:for="page in tg.paginate.pages">
	    <a py:strip="page == tg.paginate.current_page"
	        href="${tg.paginate.get_href(page)}" py:content="page"/></b><b>&nbsp;<a py:strip="tg.paginate.current_page == tg.paginate.page_count"
			href="${tg.paginate.get_href(tg.paginate.current_page+1)}" py:content="'&rarr;'" />&nbsp;<a href="${tg.paginate.get_href(tg.paginate.page_count)}" py:content="'&raquo;'" /></b></p>
	<ul>
		<li py:for="course in courses">
			<a href="${tg.url('/course/' + str(course.id))}" py:content="course.dept+' '+course.num+': '+course.name">Page Name Here.</a>
		</li>
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
