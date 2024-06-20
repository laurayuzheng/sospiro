import os
import glob
import markdown
from xml.dom import minidom

layout_html = "content/_layout.html"

# main navbar pages
for f in glob.iglob('content/*.md'):
    with open(f, 'r') as file:
        raw = file.read()
        html = markdown.markdown(raw)

    file_name = os.path.basename(f)
    destination = os.path.join(os.path.splitext(file_name)[0] + ".html")

    with open(layout_html, 'r') as layout_f:
        layout_contents = layout_f.read() 

    layout_contents = layout_contents.split("MAIN_INFO_HERE")
    assert len(layout_contents) == 2
    
    with open(destination, 'w') as file:
        print(f"writing to {destination}")
        file_content = html.join(layout_contents)
        file.write(str(file_content))
        
