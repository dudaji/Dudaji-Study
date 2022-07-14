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
            [" " for x in range(self.width)] for y in range(self.height)
        ]
        self.curY = 4
        self.curX = 3

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

        # Title 
        for idx, ch in enumerate(self.title):
            self.window[0][3+idx] = ch
        
        # Message
        for idx, ch in enumerate(self.message):
            self.window[2][3+idx] = ch

        for y in range(self.height):
            for x in range(self.width):
                print(self.window[y][x], end='')
            print()

    def createButton(self, parent, ypos: int, xpos: int, text: str) -> Button:
        return WindowsButton(parent, ypos, xpos, text)

    def createCheckbox(self, parent, text: str) -> Checkbox:
        return WindowsCheckbox(parent, text)
    
    def renderItem(self, item):
        if hasattr(item, 'ypos') and hasattr(item, 'xpos'):
            xpos = item.xpos
            ypos = item.ypos
            moveCursor = False
        else:
            xpos = self.curX
            ypos = self.curY
            moveCursor = True

        for y, line in enumerate(item.box):
            for x, ch in enumerate(line):
                if 0 <= ypos + y < self.height and 0 <= xpos + x < self.width:
                    self.window[ypos+y][xpos+x] = ch
        
        if moveCursor:
            self.curY += item.height + 1