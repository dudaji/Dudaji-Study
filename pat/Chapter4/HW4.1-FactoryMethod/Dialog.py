from abc import ABC, abstractmethod
from Button import Button

class Dialog(ABC):

    def __init__(self, title: str):
        self.title = title

    def renderWindow(self):
        print(self.title)
        print('-' * 40)
        print()

        okButton = self.createButton('OK', 1)
        okButton.render()

        print()
        print('-' * 40)

    @abstractmethod
    def createButton(self, text: str, padding: int = 0) -> Button:
        pass
