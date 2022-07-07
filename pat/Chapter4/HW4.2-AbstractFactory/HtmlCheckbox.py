from Checkbox import Checkbox

class HtmlCheckbox(Checkbox):

    def __init__(self, parent, text: str):
        super().__init__(parent, text)

    def render(self):
        print(f'<input type="checkbox" />{self.text}')