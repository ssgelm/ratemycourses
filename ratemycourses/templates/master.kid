<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<?python import sitetemplate
from cherrypy import request as cp_request
from cherrypy import session as cp_session
?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="sitetemplate">

<head py:match="item.tag=='{http://www.w3.org/1999/xhtml}head'" py:attrs="item.items()">
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
    <title py:replace="''">Your title goes here</title>
    <meta py:replace="item[:]" name="description" content="master template"/>
    <link rel="stylesheet" type="text/css" media="screen" href="/static/css/newstyle.css"
        py:attrs="href=tg.url('/static/css/newstyle.css')"/>
</head>

<body py:match="item.tag=='{http://www.w3.org/1999/xhtml}body'" py:attrs="item.items()">
	<div id="wrapper-header">
		<div id="header">
			<div py:if="tg.config('identity.on') and not defined('logging_in')" id="pageLogin">
		        <span py:if="not tg.identity.anonymous" id="outline">
		            Logged in as: ${tg.identity.user.display_name+' ('+tg.identity.user.user_name+')' or tg.identity.user.user_name}
		        </span>
		    </div>
			<h1><a href="${tg.url('/')}">RateMyCourses</a></h1>
		</div>
	</div>
		
	<div id="wrapper-menu">
		<div id="menu">
			<ul>
    			<li><a href="${tg.url('/')}">Home</a></li>
				<li><a href="${tg.url('/courses')}">Courses</a></li>
				<li><a href="${tg.url('/tags')}">Tags</a></li>
				<!--<li><a href="${tg.url('/locker')}">Locker</a></li>-->
				<span py:if="tg.config('identity.on') and not defined('logging_in')" py:strip="True">
					<span py:if="tg.identity.anonymous" py:strip="True">
						<li><a href="${tg.url(tg.identity.login_url)}">Login</a></li>
					</span>
					<span py:if="not tg.identity.anonymous" py:strip="True">
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
		<div style="float: right;">
			<a href="${tg.url('/advsearch')}">Advanced Search</a>
		</div>
		</div>
	</div>

    <div id="content">
		<!-- Flash blocks -->
		<div id="status_block" class="flash"
            py:if="value_of('tg_flash', None)" py:content="tg_flash"></div>
		<div py:if="cp_session.has_key('flash2')" id="flash2">
			<div py:for="message in cp_session.get('flash2')" class="message ${message.css}" id="flash2_${message.md5}">
				<div py:if="message.hideable" class="hide">
					<a href="#" onclick="javascript:MochiKit.Visual.fade('flash2_${message.md5}', {'duration':0.25});">Hide</a>
				</div>
				<span py:if="message.html" py:content="XML(message.message)" />
				<span py:if="not message.html" py:content="message.message" />
			</div>
		</div>
		
        <div py:replace="[item.text]+item[:]">page content</div>
    </div>

    <div id="footer">
        <p><b>Disclaimer:</b> This website is a demonstration of our term project for CS125: Human-Computer Interaction in Spring 2010. It is based on research of computer-supported collaboration and interface design. It is a work in progress and not all features will work as planned. We're working on it.</p>
		<p><a href="/static/feedback.html" target="_blank">Questions/Comments/Bugs? Click here</a>. &copy; 2010 Stephen Gelman, Ravi Kotecha, Andy Lewis, Kevin Weaver</p>
    </div>
</body>

</html>
