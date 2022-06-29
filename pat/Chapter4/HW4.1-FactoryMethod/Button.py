from abc import ABC, abstractmethod

class Button(ABC):

    def __init__(self, text: str, padding: int = 0):
        self.text = text
        self.padding = padding

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass

