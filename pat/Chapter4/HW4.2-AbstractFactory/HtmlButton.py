from Button import Button

class HtmlButton(Button):

    def __init__(self, parent, ypos: int, xpos: int, text: str):
        super().__init__(parent, ypos, xpos, text)

    def render(self):
        style = f' style="position: absolute; top: {self.ypos * 10}px; left: {self.xpos * 10}px;"'
        print(f'<button{style}>{self.text}</button>')