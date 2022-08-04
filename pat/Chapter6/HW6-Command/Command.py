from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, editor):
        self.editor = editor
        self._backup = ""

    def backup(self):
        self._backup = self.editor.textedit.toPlainText()

    def undo(self):
        self.editor.textedit.setText(self._backup)

    @abstractmethod
    def execute(self):
        pass
