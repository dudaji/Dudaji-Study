from WindowsButton import WindowsButton
from WindowsCheckbox import WindowsCheckbox
from Button import Button
from Checkbox import Checkbox
from Dialog import Dialog


class WindowsDialog(Dialog):
    def __init__(self, title: str, message: str):
        super().__init__(title, message)
        self.width = 80
        self.height = 24
        self.window = [
            ["" for x in range(self.width)] for y in range(self.height)
        ]

    def renderWindow(self):
        for item in self.items:
            item.render()
        
        for x in range(self.width):
            self.window[0][x] = '-'
            self.window[self.height-1][x] = '-'
        
        for y in range(self.height):
            self.window[y][0] = '|'
            self.window[y][self.width-1] = '|'
        
        self.window[0][0] = '+'
        self.window[0][self.width-1] = '+'
        self.window[self.height-1][0] = '+'
        self.window[self.height-1][self.width-1] = '+'

        for y in range(self.height):
            for x in range(self.width):
                print(self.window[y][x], end='')
            print()

    def createButton(self, parent, ypos: int, xpos: int, text: str) -> Button:
        return WindowsButton(parent, ypos, xpos, text)

    def createCheckbox(self, parent, text: str) -> Checkbox:
        return WindowsCheckbox(parent, text)
