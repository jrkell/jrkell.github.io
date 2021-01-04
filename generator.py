import json
from string import Template

#### SETTINGS ####
debug = True

launcher_file = "index.html"
template_file = "template.html"
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

out = open(launcher_file, 'w')
template = open(template_file, 'r')
template_contents = template.read()
message = template_contents.format(links_section=links_section)

out.write(message)
out.close()
template.close()