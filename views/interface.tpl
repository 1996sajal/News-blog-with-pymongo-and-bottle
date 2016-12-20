<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" href="interface.css">
	
</head>
<body>

	<div class="container">
		%for news in articles:
		<div class="news-block">
			<div class="news-image"><img src={{news["urlToImage"]}} height="512" alt=""></div>
			<div class="news">
				<p class="news-author">By: <span style="font-weight: 700">{{news["author"]}}</span></p>
				<h2 class="news-headline">{{news["title"]}}</h2>
				<p class="news-desc">{{news["description"]}}<span style="font-weight: 700; color: #d56;" class="read-more"><a href={{news["url"]}}>  Read More</span></p>
				<p class="news-date">{{news["publishedAt"]}}<span style="float: right; font-weight: 400"></span></p>
			</div>
		</div>
		%end
	</div>
	
</body>
</html>
