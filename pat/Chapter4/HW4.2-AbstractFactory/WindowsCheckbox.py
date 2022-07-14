from Checkbox import Checkbox


class WindowsCheckbox(Checkbox):
    def __init__(self, parent, text: str):
        super().__init__(parent, text)
        self.width = len(self.text) + 2
        self.height = 1
        content = "_ " + self.text
        self.box = [content]

    def render(self):
        for y, line in enumerate(self.box):
            for x, ch in enumerate(line):
                pass
