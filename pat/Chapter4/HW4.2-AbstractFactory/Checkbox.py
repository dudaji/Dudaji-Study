from abc import ABC, abstractmethod


class Checkbox(ABC):
    def __init__(self, parent, text: str):
        self.parent = parent
        self.text = text
        self.parent.items.append(self)

    @abstractmethod
    def render(self):
        pass
