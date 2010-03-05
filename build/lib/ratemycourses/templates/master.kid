<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<?python import sitetemplate ?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="sitetemplate">

<head py:match="item.tag=='{http://www.w3.org/1999/xhtml}head'" py:attrs="item.items()">
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
    <title py:replace="''">Your title goes here</title>
    <meta py:replace="item[:]" name="description" content="master template"/>
    <style type="text/css" media="screen">
        #pageLogin
        {
            font-family: verdana;
            text-align: right;
			width: 777px;
			margin: 0 auto 0 auto;
        }
    </style>
    <link rel="stylesheet" type="text/css" media="screen" href="../static/css/style.css"
        py:attrs="href=tg.url('/static/css/style.css')"/>
</head>

<body py:match="item.tag=='{http://www.w3.org/1999/xhtml}body'" py:attrs="item.items()">
    <div py:if="tg.config('identity.on') and not defined('logging_in')" id="pageLogin">
        <span py:if="not tg.identity.anonymous">
            Logged in as: ${tg.identity.user.display_name or tg.identity.user.user_name}
        </span>
    </div>

    <div id="header"><a href="${tg.url('/')}" id="logo">RateMyCourses</a></div>

    <div id="main_content">
		<div id="sidebar">
			<form method="get" action="/search">
				<input name="search" style="width: 90px" value="Search" onfocus="this.value=''"/>
			</form>
	    	<a href="${tg.url('/')}">Home</a><br />
			<a href="${tg.url('/courses')}">Courses</a><br />
			<a href="${tg.url('/tags')}">Tags</a><br />
			<a href="${tg.url('/locker')}">Locker</a><br />
			<span py:if="tg.config('identity.on') and not defined('logging_in')">
				<span py:if="tg.identity.anonymous">
					<a href="${tg.url(tg.identity.login_url)}">Login</a>
				</span>
				<span py:if="not tg.identity.anonymous">
					<a href="${tg.url('/editprofile')}">Edit Profile</a><br />
					<a href="${tg.url('/logout')}">Logout</a>
				</span>
			</span>
		</div>

		<div id="status_block" class="flash"
            py:if="value_of('tg_flash', None)" py:content="tg_flash"></div>
        <div py:replace="[item.text]+item[:]">page content</div>
    </div>

    <div id="footer">
        <p>Disclaimer: This website is a demonstration of our term project for CS118: Computer-Supported Cooperation.  It is a work in progress and not all features will work as planned, though we're working on it.</p>
		<p>&copy; 2009 Stephen Gelman, Ravi Kotecha, Andy Lewis</p>
    </div>
</body>

</html>
