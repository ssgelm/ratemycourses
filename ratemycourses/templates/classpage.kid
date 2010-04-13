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
	<link rel="stylesheet" href="/static/css/mediaboxAdvWhite.css" type="text/css" media="screen" />
	<script src="/static/javascript/mootools-1.2.4-core-yc.js" type="text/javascript"></script>
	<script src="/static/javascript/mediaboxAdv-1.2.0.js" type="text/javascript"></script> 
</head>
<body>

<div>
    <div style="display: inline; float: left; width: 70%">
	<h1><span py:replace="name">Class Name</span></h1>
	<h2><span py:replace="dept">DEPT</span> <span py:replace="num">NUM</span><!--&nbsp;-&nbsp;<span style="font: x-small 'Lucida Grande', 'Lucida Sans Unicode', geneva, verdana, sans-serif"><a href="${tg.url('/addtolocker/' + classid)}">Add to my locker</a></span>--></h2>
	</div>
	<div id="avgRating" style="float: right; width: 30%; padding-top: 10px;">${XML(avg_score)}</div>
	<hr style="clear:both;" />
	<p style="margin: 2px auto;"><span style="margin-right: 12px;" py:for="i in range(0,len(sysTags))"><a class="tag" href="${tg.url('/tag/' + str(sysTags[i]))}" py:content="sysTags[i]">Tag</a></span></p>
	<hr />
	<p><span py:replace="description">Course description</span></p>
	<p><b>Tagged as:</b>
	    <span>
		    <span class="tag" style="line-height: 100%;" py:for="i in range(0,len(tags))">
		        <a class="tag" href="${tg.url('/tag/' + str(tags[i].name))}" py:content="tags[i].name">Tag</a>
		        <span class="vote">
					<a class="vote" href="#"><img class="vote" src="${tg.url('/static/images/up-arrow.png')}" /></a>
		            <a class="vote" href="#"><img class="vote" src="${tg.url('/static/images/down-arrow.png')}" /></a>
		        </span>
		        <span py:if="not tg.identity.anonymous and tg.identity.user.admin">
		            <a href="${tg.url('/untagcourse/' + str(classid) + '/' + str(tags[i].name))}"><img class="vote" style="width 15px; height: 15px; vertical-align:-20%;" src="${tg.url('/static/images/error.png')}" /></a>
		        </span>
		    </span>
		    <br /><a href="${tg.url('/addtag/' + str(classid))}" rel="lightbox" title="Add tag">Add Tag...</a>
		</span>
	</p>
	<p><b>People who took this course also took:</b><br />
	<ul>
		<li py:for="course in relatedCourses">
			<a href="${tg.url('/course/' + str(course.id))}" py:content="course.dept+' '+course.num+': '+course.name">Page Name Here.</a>
		</li>
	</ul></p>

	<!--<p><b>Reviews:</b></p>
	<div py:for="i in range(0,len(reviews))" id="review">
		<p>Rating: <span py:for="j in range(0,reviews[i].score)"><img src="/static/images/star.jpg" /></span><span py:for="j in range(0,5-reviews[i].score)"><img src="/static/images/nostar.jpg" /></span><br />
		Review by: <a href="${tg.url('/user/' + str(reviews[i].reviewer.id))}" py:content="reviews[i].reviewer.display_name">User</a> on ${reviews[i].created.ctime()}</p>
		<p><span py:replace="reviews[i].contents">Review goes here</span></p>
		<p><span style="font-size: 10px">The reviewer took the course with <span py:replace="reviews[i].professor">None</span>.<br />
		<i><span py:replace="reviews[i].num_liked">0</span> out of <span py:replace="reviews[i].num_rated">0</span> found this review useful</i><br />
		Did you find this review useful? <a href="${tg.url('/likedreview/' + str(reviews[i].id) + '/' + str(classid))}">Yes</a> <a href="${tg.url('/dislikedreview/' + str(reviews[i].id) + '/' + str(classid))}">No</a>&nbsp;|&nbsp;Is this review inappropriate? <a href="${tg.url('/flagreview/' + str(reviews[i].id) + '/' + str(classid))}">Report</a>
		<span py:if="not tg.identity.anonymous and tg.identity.user.admin"><br /><a href="${tg.url('/deletereview/' + str(classid) + '/' + str(reviews[i].id))}">Remove this review</a></span></span></p>
	</div>
	<a href="${tg.url('/addreview/'+classid)}">Add review</a>-->

</div>

</body>
</html>
