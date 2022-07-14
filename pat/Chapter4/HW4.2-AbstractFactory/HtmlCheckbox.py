from Checkbox import Checkbox


class HtmlCheckbox(Checkbox):
    def render(self):
        print(f'<input type="checkbox" />{self.text}')
