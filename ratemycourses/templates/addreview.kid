<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>RateMyCourses: Add review for <span py:replace="dept">DEPT</span> <span py:replace="num">NUM</span> - <span py:replace="name">Class Name</span></title>
</head>
<body>

<div>
    
	<h1>Add review for <span py:replace="dept">DEPT</span> <span py:replace="num">NUM</span> - <span py:replace="name">Class Name</span></h1>
	<br />
    

	<p py:content="form(formclassid)">Review form</p>

</div>

</body>
</html>
