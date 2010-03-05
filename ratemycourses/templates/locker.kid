<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>RateMyCourses: ${tg.identity.user.display_name or tg.identity.user.user_name}'s Locker</title>
</head>
<body>

<div>

	<h1>${tg.identity.user.display_name or tg.identity.user.user_name}'s Locker</h1>
	<hr />
		<ul>
		    <li py:for="i in locker">
				<a href="${tg.url('/course/' + str(i.id))}" py:content="i.dept+' '+i.num+': '+i.name">Page Name Here.</a>
			</li>
		</ul>
		<p><a href="${tg.url('/clearlocker')}">Clear Locker</a></p>

</div>

</body>
</html>
