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
	
	${courseTree()}
	
</div>

</body>
</html>
