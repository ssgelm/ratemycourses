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
	<ul>
		<li py:for="i in range(0,len(idlist))">
			<a href="${tg.url('/course/' + str(idlist[i]))}" py:content="deptlist[i]+' '+numlist[i]+': '+namelist[i]">Page Name Here.</a>
		</li>
	</ul>

</div>

</body>
</html>
