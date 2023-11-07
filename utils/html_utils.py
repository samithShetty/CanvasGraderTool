from html.parser import HTMLParser

class HTMLToText(HTMLParser):
    
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.text = ""
    
    def handle_data(self, data: str) -> None:
        self.text += data
        return super().handle_data(data)

html_parser = HTMLToText()

def html_to_text(html):
    html_parser.text = ""
    html_parser.feed(html)
    return html_parser.text