from Button import Button


class HtmlButton(Button):
    def render(self):
        style = f' style="position: absolute; top: {self.ypos * 10}px; left: {self.xpos * 10}px;"'
        print(f"<button{style}>{self.text}</button>")
