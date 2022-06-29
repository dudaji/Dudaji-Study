from Button import Button

class WindowsButton(Button):

    def __init__(self, text: str, padding: int = 0):
        super().__init__(text, padding)

    def render(self):
        width = len(self.text) + self.padding * 2
        print('+' + '-' * width + '+')
        for i in range(self.padding):
            print('|' + ' ' * width + '|')
        print('|' + ' ' * self.padding + self.text + ' ' * self.padding + '|')
        for i in range(self.padding):
            print('|' + ' ' * width + '|')
        print('+' + '-' * width + '+')

    def onClick(self):
        print('Click!!')
