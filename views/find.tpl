<html>
<body style="background-color:#E9967A;">
    <h1>Welcome to NewSter</h1>
    %for news in source:
    <p>
    <h3>{{news["title"]}}</h3>
    <h4>-By {{news["author"]}}</h4>
    <h5 style="background-color:#A7F0F5;"><blockquote>{{news["description"]}}</blockquote></h5>
    <img src={{news["urlToImage"]}} style="width:150px;height:150px;">
    <br><b>For further info <a href={{news["url"]}}>{{news["url"]}}</a></b>
    <br>
    <hr style = 'background-color:#D7BDE2; border-width:0; color:#D7BDE2; height:10px; lineheight:0; display: inline-block; text-align: left; width:50%;' />
    </p>
</body>
</html>
