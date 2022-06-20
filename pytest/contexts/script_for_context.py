def create_html_page():
    page_text = "<b>Hello world</b>"
    
    with open("index.html", "w+", encoding="utf-8") as file:
        file.write(page_text)