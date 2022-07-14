from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, parent, ypos: int, xpos: int, text: str):
        self.parent = parent
        self.ypos = ypos
        self.xpos = xpos
        self.text = text
        self.parent.items.append(self)

    @abstractmethod
    def render(self):
        pass
