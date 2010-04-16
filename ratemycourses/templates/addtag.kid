<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML#.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#">

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
	<link rel="stylesheet" type="text/css" media="screen" href="/static/css/newstyle.css" py:attrs="href=tg.url('/static/css/newstyle.css')"/>
	<link media="all" href="/tg_widgets/turbogears.widgets/autocompletefield.css" type="text/css" rel="stylesheet" /> 
    <script src="/tg_widgets/turbogears.widgets/autocompletefield.js" type="text/javascript"></script>
	<script src="/tg_widgets/tgmochikit/packed/MochiKit/MochiKit.js" type="text/javascript"></script> 
    <title>Add tag for ${course.dept+" "+course.num}</title>
</head>
<body class="whitebg">
	<p>To add a tag, please either select it from the list or type it in the box below and click "Add Tag".  If the tag does not already exist it will be created.</p>
	<form action="/tagcourse" type="GET">
		${acfield.display()}
		<input type="hidden" name="courseid" value="${course.id}" />
		<input type="Submit" value="Add Tag" />
	</form>
	<p>Available tags:</p>
	<span class="tag" py:for="tag in tags">
		<a class="addtag" href="${'/tagcourse?courseid=' + str(course.id) + '&amp;tag.text=' + tag.name}" py:content="tag.name">Tag</a>
	</span>
</body>
</html>
