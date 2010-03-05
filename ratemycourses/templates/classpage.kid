<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>RateMyCourses: <span py:replace="dept">DEPT</span> <span py:replace="num">NUM</span> - <span py:replace="name">Class Name</span></title>
<script language="javascript">
function nav()
        {
                var w = document.addtag.tag.selectedIndex;
                var url_add = document.addtag.tag.options[w].value;
				if(url_add == 'newtag'){
					url_add=prompt("Tag Name:", "");
				}
				if(url_add !== 'null'){
				if(url_add !== 'undefined'){
                	window.location.href = '${tg.url('/tagcourse/'+classid+'/')}'+url_add;
				}}
        }
</script>
</head>
<body>

<div>

	<h1><span py:replace="name">Class Name</span></h1>
	<h2><span py:replace="dept">DEPT</span> <span py:replace="num">NUM</span>&nbsp;-&nbsp;<span style="font: x-small 'Lucida Grande', 'Lucida Sans Unicode', geneva, verdana, sans-serif"><a href="${tg.url('/addtolocker/' + classid)}">Add to my locker</a></span></h2>
	<hr />
	<p><span py:replace="description">Course description</span></p>
	<p><b>Tags:</b>
		<span py:for="i in range(0,len(tags))"><a href="${tg.url('/tag/' + str(tags[i].name))}" py:content="tags[i].name">Tag</a><span py:if="not tg.identity.anonymous and tg.identity.user.admin">&nbsp;<a href="${tg.url('/untagcourse/' + str(classid) + '/' + str(tags[i].name))}">(X)</a></span>, </span>
		<form method="get" action="${tg.url('/tagcourse/' + str(classid) + '/')}" name="addtag">
			<select name="tag" onChange="nav()">
				<option value=''>Add Tag...</option>
				<option py:for="i in alltags" value="${i}" py:content="i">TAG</option>
				<option value="newtag">New Tag...</option>
			</select>
		</form>
	</p>
	<p>Average review: ${XML(avg_score)}</p>
	<p><b>People who took this course also took:</b><br />
	<ul>
		<li py:for="course in relatedCourses">
			<a href="${tg.url('/course/' + str(course.id))}" py:content="course.dept+' '+course.num+': '+course.name">Page Name Here.</a>
		</li>
	</ul></p>

	<p><b>Reviews:</b></p>
	<div py:for="i in range(0,len(reviews))" id="review">
		<p>Rating: <span py:for="j in range(0,reviews[i].score)"><img src="/static/images/star.jpg" /></span><span py:for="j in range(0,5-reviews[i].score)"><img src="/static/images/nostar.jpg" /></span><br />
		Review by: <a href="${tg.url('/user/' + str(reviews[i].reviewer.id))}" py:content="reviews[i].reviewer.display_name">User</a> on ${reviews[i].created.ctime()}</p>
		<p><span py:replace="reviews[i].contents">Review goes here</span></p>
		<p><span style="font-size: 10px">The reviewer took the course with <span py:replace="reviews[i].professor">None</span>.<br />
		<i><span py:replace="reviews[i].num_liked">0</span> out of <span py:replace="reviews[i].num_rated">0</span> found this review useful</i><br />
		Did you find this review useful? <a href="${tg.url('/likedreview/' + str(reviews[i].id) + '/' + str(classid))}">Yes</a> <a href="${tg.url('/dislikedreview/' + str(reviews[i].id) + '/' + str(classid))}">No</a>&nbsp;|&nbsp;Is this review inappropriate? <a href="${tg.url('/flagreview/' + str(reviews[i].id) + '/' + str(classid))}">Report</a>
		<span py:if="not tg.identity.anonymous and tg.identity.user.admin"><br /><a href="${tg.url('/deletereview/' + str(classid) + '/' + str(reviews[i].id))}">Remove this review</a></span></span></p>
	</div>
	<a href="${tg.url('/addreview/'+classid)}">Add review</a>

</div>

</body>
</html>
