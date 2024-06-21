import os
import glob
import markdown
import datetime

layout_html = "content/_layout.html"
timestamp = datetime.datetime.now().strftime("%Y年%m月%d日")
footer_msg = f"Last updated on {timestamp}"

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
    file_content = html.join(layout_contents)
    layout_contents = file_content.split("FOOTER_MSG_HERE")
    assert len(layout_contents) == 2
    file_content = footer_msg.join(layout_contents)
    
    with open(destination, 'w') as file:
        print(f"writing to {destination}")
        file.write(str(file_content))
        
