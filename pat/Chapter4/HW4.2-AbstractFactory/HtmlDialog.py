from HtmlButton import HtmlButton
from HtmlCheckbox import HtmlCheckbox
from Dialog import Dialog

class HtmlDialog(Dialog):

    def __init__(self, title: str, message: str):
        super().__init__(title, message)

    def renderWindow(self):
        print('<!DOCTYPE html>\n<html>\n\n<head>')
        print(f'    <title>{self.title}</title>')
        print('</head>\n\n<body>')
        print(f'    <p>{self.message}</p>')
        for item in self.items:
            print('    ', end='')
            item.render()
        print('</body>\n\n</html>')

    def createButton(self, parent, ypos: int, xpos: int, text: str):
        return HtmlButton(parent, ypos, xpos, text)
    
    def createCheckbox(self, parent, text: str):
        return HtmlCheckbox(parent, text)