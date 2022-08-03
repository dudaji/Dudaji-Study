from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, editor):
        self.editor = editor

    def backup(self):
        self._backup = self.editor.textField.getText()

    def undo(self):
        self.editor.textField.setText(self._backup)

    @abstractmethod
    def execute(self):
        pass
