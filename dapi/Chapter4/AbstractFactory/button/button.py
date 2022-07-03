from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    def on_click(self):
        return type(self).__name__ + " is clicked!"
