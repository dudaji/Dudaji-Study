from re import L
from Button import Button


class WindowsButton(Button):
    def __init__(self, parent, ypos: int, xpos: int, text: str):
        super().__init__(parent, ypos, xpos, text)
        self.width = len(self.text) + 4
        self.height = 3
        border = "+" + "-" * (self.width - 2) + "+"
        content = "| " + self.text + " |"
        self.box = [border, content, border]

    def render(self):
        for y, line in enumerate(self.box):
            for x, ch in enumerate(line):
                pass
