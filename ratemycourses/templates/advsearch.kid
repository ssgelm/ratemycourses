<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>Welcome to RateMyCourses</title>
</head>
<body>

<div>
    
	<h1>Advanced Search</h1>
    
    <div style="width: 50%; float: left;">
		<h2>Tags</h2>
		<form action="/advsearch" method="post">
			<ul>
				<li py:for="tag in tags">
					<label><input type="checkbox" name="searchtags" value="${tag.name}"/><span py:content="tag.name">Tag</span></label>
				</li>
			</ul>
			<input type="submit" name="submit" value="Search" />
		</form>
	</div>
	<div style="width: 50%; float: right;">
		<h2>Results</h2>
		<ul>
			<li py:for="result in results" py:content="result.name">
				Result
			</li>
		</ul>
	</div>
	<div style="clear: both;"></div>
	

</div>

</body>
</html>
