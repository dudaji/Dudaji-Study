from Button import Button

class HtmlButton(Button):

    def __init__(self, text: str, padding: int = 0):
        super().__init__(text, padding)

    def render(self):
        if self.padding == 0:
            style = ''
        else:
            style = f' style="padding: {self.padding}px;"'
        print(f'<button{style}>{self.text}</button>')

    def onClick(self):
        print('Click!')

