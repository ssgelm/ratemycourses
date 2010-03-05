<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>Welcome to RateMyCourses</title>
</head>
<body>

<div>
    
	<p>Here are the tags that are currently in the system:</p>
    
	<p>Sort by: <a href="${tg.url('/tags/name')}">Name</a>&nbsp;|&nbsp;<a href="${tg.url('/tags/popularity')}">Popularity</a></p>

	<ul>
		<li py:for="tag in tags">
			<a href="${tg.url('/tag/' + tag[0])}" py:content="tag[0]+' ('+str(tag[1])+')'">Page Name Here.</a>
		</li>
	</ul>

</div>

</body>
</html>
