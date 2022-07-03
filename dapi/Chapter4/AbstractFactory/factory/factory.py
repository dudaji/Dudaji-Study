from abc import ABC, abstractmethod
from button.button import Button
from checkbox.checkbox import CheckBox


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass
