<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>RateMyCourses: Edit <span py:replace="tagName">TAG</span></title>
</head>
<body>

<div>

    <h1>Editing: <span py:replace="tagName">Tag</span></h1>
    <form action="/savetag" method="post">
        <input type="hidden" name="tagName" value="${tagName}"/>
        <textarea name="data" py:content="description" rows="10" cols="60"/>
        <input type="submit" name="submit" value="Save"/>
    </form>

</div>

</body>
</html>
