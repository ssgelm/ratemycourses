<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<?python import sitetemplate ?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="sitetemplate">

<head py:match="item.tag=='{http://www.w3.org/1999/xhtml}head'" py:attrs="item.items()">
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
    <title py:replace="''">Your title goes here</title>
    <meta py:replace="item[:]" name="description" content="master template"/>
    <!-- <style type="text/css" media="screen">
        #pageLogin
        {
            font-family: verdana;
            text-align: right;
			width: 777px;
			margin: 0 auto 0 auto;
        }
    </style> -->
    <link rel="stylesheet" type="text/css" media="screen" href="/static/css/newstyle.css"
        py:attrs="href=tg.url('/static/css/newstyle.css')"/>
</head>

<body py:match="item.tag=='{http://www.w3.org/1999/xhtml}body'" py:attrs="item.items()">
    <div py:if="tg.config('identity.on') and not defined('logging_in')" id="pageLogin">
        <span py:if="not tg.identity.anonymous">
            Logged in as: ${tg.identity.user.display_name or tg.identity.user.user_name}
        </span>
    </div>

	<div id="wrapper-header">
		<div id="header">
			<h1>RateMyCourses</h1>
		</div>
	</div>
		
	<div id="wrapper-menu">
		<div id="menu">
			<ul>
    			<li><a href="${tg.url('/')}">Home</a></li>
				<li><a href="${tg.url('/courses')}">Courses</a></li>
				<li><a href="${tg.url('/tags')}">Tags</a></li>
				<li><a href="${tg.url('/locker')}">Locker</a></li>
				<span py:if="tg.config('identity.on') and not defined('logging_in')">
					<span py:if="tg.identity.anonymous">
						<li><a href="${tg.url(tg.identity.login_url)}">Login</a></li>
					</span>
					<span py:if="not tg.identity.anonymous">
						<li><a href="${tg.url('/editprofile')}">Edit Profile</a></li>
						<li><a href="${tg.url('/logout')}">Logout</a></li>
					</span>
				</span>
			</ul>
		<div id="searchbox">
			<form method="get" action="/search">
				<input name="search" id="s" value="Search..." onfocus="this.value=''"/>
				<input type="image" src="${tg.url('/static/images/searchbtn.png')}" width="27" height="24" id="go" alt="Search" title="Search" name="go" />
			</form>
		</div>
		</div>
	</div>

    <div id="content">
		<div id="status_block" class="flash"
            py:if="value_of('tg_flash', None)" py:content="tg_flash"></div>
        <div py:replace="[item.text]+item[:]">page content</div>
    </div>

    <div id="footer">
        <p>Disclaimer: This website is a demonstration of our term project for CS125: Human-Computer Interaction.  It is a work in progress and not all features will work as planned, though we're working on it.</p>
		<p>&copy; 2010 Stephen Gelman, Ravi Kotecha, Andy Lewis, Kevin Weaver</p>
    </div>
</body>

</html>
