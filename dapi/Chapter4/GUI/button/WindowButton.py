from button.Button import Button


class WindowButton(Button):
    def render(self):
        return "Window Button"

    def onClick(self):
        return "Window Button is clicked!"
