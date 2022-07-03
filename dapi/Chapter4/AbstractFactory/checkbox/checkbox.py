from abc import ABC, abstractmethod


class CheckBox(ABC):
    def __init__(self):
        self._is_checked = False

    @abstractmethod
    def render(self):
        pass

    def on_check(self):
        if self._is_checked:
            self._is_checked = False
        else:
            self._is_checked = True
