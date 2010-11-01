import webbrowser
# html code to overlap three pictures
#
# if you supply your own pictures, you may have to change
#
# widths, heights and absolute positions
#
str1 = """
<html>
<head>
<title>Senate Race: """ + stateID + """</title>
</head>
<body bgcolor="white">
<!-- you may need to supply your own image files -->
<!-- and adjust their widths and heights accordingly -->

<div style="position:absolute; left:250; top:25; width:100; height:125">
<img id = "image1" width = 100 height = 125 src = "dem.png">
</div>
 
<div style="position:absolute; left:500; top:25; width:100; height:125">
<img id = "image2" width = 100 height = 125 src = "gop.png">
</div>
 
<div style="position:absolute; left:750; top:25; width:100; height:125">
<img id = "image3" width = 100 height = 125 src = "ind.png">
</div>
 
<div style="position:absolute; left:150; top:150; width:800; height:400">
<img id = "image3" width = 800 height = 400 src = "poll_fig.png">
</div>

</body>
</html>"""
 
# write the html file to the working folder
fout = open("senate_race.htm", "w")
fout.write(str1)
fout.close()
 
# now open your web browser to run the file
webbrowser.open("senate_race.htm")