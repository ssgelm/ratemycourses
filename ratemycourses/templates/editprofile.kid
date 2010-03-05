<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>RateMyCourses: <span py:replace="username">USER</span>'s Profile</title>
</head>
<body>

<div>
    
	<h1><span py:replace="username">USER</span>'s Profile</h1>
	<br />
    
	<table cellpadding="2" cellspacing="0" border="0">
	<form action="/saveprofile" method="post">
		<tr><td>Alias:</td> <td><input name="alias" value="${alias}" /></td></tr>
		<tr><td valign="top">About Me:</td><td><textarea name="aboutMe" rows="7" cols="50">${aboutMe}</textarea></td></tr>
		<tr><td><input type="submit" name="submit" value="Submit"/></td></tr>
	</form>
	</table>

</div>

</body>
</html>
