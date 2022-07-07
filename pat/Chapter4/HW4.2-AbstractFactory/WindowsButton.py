from Button import Button

class WindowsButton(Button):

    def __init__(self, parent, ypos: int, xpos: int, text: str):
        super().__init__(text, parent, ypos, xpos, text)
        self.width = len(self.text) + 4
        self.box = []

    def render(self):
        for y, line in enumerate(self.box):
            for x, ch in enumerate(line):
                
        width = len(self.text) + 2
        print('+' + '-' * width + '+')
        for i in range(self.padding):
            print('|' + ' ' * width + '|')
        print('|' + ' ' * self.padding + self.text + ' ' * self.padding + '|')
        for i in range(self.padding):
            print('|' + ' ' * width + '|')
        print('+' + '-' * width + '+')

    def onClick(self):
        print('Click!!')
