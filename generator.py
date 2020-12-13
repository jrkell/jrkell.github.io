import json
from string import Template

#### SETTINGS ####
debug = True

launcher_file = "index.html"
bookmarks_file = "bookmarks.json"
##################

#### CODE ####
def generateLinks():                       
    output = "<div class='links-container'>"
    f = open('bookmarks.json', 'r')
    bookmarks_json = f.read()
    if debug: print(bookmarks_json)
    bookmarks_dict = json.loads(bookmarks_json)
    if debug: print(bookmarks_dict)
    for col in bookmarks_dict["columns"]:
        output += """<div class="main">
                        <ul class="hyperlinks">
                        <li id="main-h">%s</li>
                """ % (col["column_title"])
        for item in col["links"]:
            if item["type"] == "sub_title":
                output += "<li class='separators'>---%s---</li>" % (item["text"])
            elif item["type"] == "link":
                output += "<li><a href='%s'>%s</a></li>" % (item["url"], item["text"])

        output += "</ul></div>"
    output += "</div>"
    if debug: print(output)
    return output


links_section = generateLinks()

f = open('test.html', 'w')
message = """<html>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <meta http-equiv='X-UA-Compatible' content='ie=edge'>
    <link rel='stylesheet' href='main.css'>
    <link rel='stylesheet' href='reset.css'>
    <title>>> launcher <<</title>
</head>
<body>
    <div id='outer'>
        <div id='middle'>

            <div id='themes'>
                <button class='button' type='button' onclick='cycleThemes()'>cycle_themes</button> 
            </div>

            <div class='terminal-screen' id='inner'>
                <!-- username with cursor -->
                <div class='user'>
                    <a class='unix-user'>jared</a>
                    <a class='unix-syntax1'>@</a>
                    <a class='PC-name'>jared-desktop</a>
                    <a class='unix-syntax2'>&#126;</a>
                    <!--  <a class='cursor'>|</a> -->
                </div>

                <!-- links with sections -->
                {links_section}

                <!-- search with duckduckgo-->
                <div id='search'>
                    <a class='unix-user'>Search</a>
                    <a class='unix-syntax1'>@</a>
                    <a class='PC-name'>DuckDuckGo.com</a>
                    <a class='unix-syntax2'>&#126;</a>
                    <form id='search-bar' method='get' action='http://duckduckgo.com/'>
                        <input type='text' name='q' placeholder='' autofocus />
                    </form>
                </div>

            </div><!-- middle -->
        
        <!-- music stuff to add
            <div class='music-embed'>
                <iframe width='100%' height='300' scrolling='no' frameborder='no' allow='autoplay' src='https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/327432184&color=%23c75457&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'></iframe>
            </div>
            -->
        </div>
    </div><!-- outer -->
    <script src='themes.js'></script>
</body>
</html>
""".format(links_section=links_section)


f.write(message)
f.close()