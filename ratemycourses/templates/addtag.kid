<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML#.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#">

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
	<link media="all" href="/tg_widgets/turbogears.widgets/autocompletefield.css" type="text/css" rel="stylesheet" /> 
    <script src="/tg_widgets/turbogears.widgets/autocompletefield.js" type="text/javascript"></script>
	<script src="/tg_widgets/tgmochikit/packed/MochiKit/MochiKit.js" type="text/javascript"></script> 
    <title>Add tag for ${course.dept+" "+course.num}</title>
</head>
<body>
	<form action="/tagcourse" type="GET">
		${acfield.display()}
		<input type="hidden" name="courseid" value="${course.id}" />
		<input type="Submit" name="Submit" />
	</form>
</body>
</html>