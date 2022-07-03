from button.Button import Button


class HtmlButton(Button):
    def render(self):
        return "<button>HTML Button</button>"

    def onClick(self):
        return "HTML Button is clicked!"
