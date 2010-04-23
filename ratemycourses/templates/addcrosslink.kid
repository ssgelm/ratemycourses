<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML#.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#">

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
	<link rel="stylesheet" type="text/css" media="screen" href="/static/css/newstyle.css" py:attrs="href=tg.url('/static/css/newstyle.css')"/>
	<link rel="stylesheet" type="text/css" media="screen" href="/static/css/flexselect.css" py:attrs="href=tg.url('/static/css/flexselect.css')"/>
	<script src="/static/javascript/jquery-1.4.2.min.js" type="text/javascript"></script> 
	<script src="/static/javascript/liquidmetal.js" type="text/javascript"></script> 
	<script src="/static/javascript/jquery.flexselect.js" type="text/javascript"></script>
	<script type="text/javascript"> 
		$(document).ready(function() {
			$("select.flexselect").flexselect();
			//$("input:text:enabled:first").focus();
		});
	</script>
    <title>Add CrossLink for ${course.dept+" "+course.num}</title>
</head>
<body class="whitebg">
	<p>To add a CrossLink, please start typing the department, name, or number of the course in the box below.  When you see the course you want, click it or press enter to select it.  Then, enter a description that explains why the courses are related and click "Add CrossLink."</p>
	<form action="/crosslinkcourse" type="POST">
		<input type="hidden" name="course1" value="${course.id}" />
		<select class="flexselect" id="course2" name="course2">
			<option value=""></option>
			<option py:for="course2 in all_courses" value="${course2.id}">${course2.dept} ${course2.num}: ${course2.name}</option>
		</select>
		<br /><br />
		<label for="description">CrossLink Description: </label><br /><textarea name="description" style="width:350px; height:75px;"/>
		<br /><br />
		<input type="Submit" value="Add CrossLink" />
	</form>
</body>
</html>
