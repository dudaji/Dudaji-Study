from abc import ABC, abstractmethod
from Button import Button
from Checkbox import Checkbox


class Dialog(ABC):
    def __init__(self, title: str, message: str):
        self.title = title
        self.message = message
        self.items = []
        self.createCheckbox(self, "Checkbox1")
        self.createCheckbox(self, "Checkbox2")
        self.createButton(self, 15, 5, "OK")
        self.createButton(self, 10, 35, "Cancel")

    @abstractmethod
    def renderWindow(self):
        pass

    @abstractmethod
    def createButton(self, parent, ypos: int, xpos: int, text: str) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self, parent, text: str) -> Checkbox:
        pass
