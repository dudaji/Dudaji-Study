from abc import ABC, abstractmethod
from editor.editor import Editor
from application.app import App


class Command(ABC):
    def __init__(self, receiver:Editor, app:App):
        self.receiver = receiver
        self.app = app
        self.backup = ""

    @abstractmethod
    def execute(self):
        pass
    
    def save_backup(self):
        self.backup = self.receiver.text
    
    def undo(self):
        self.receiver.text = self.backup


class CopyCommand(Command):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.receiver.get_selection()


class CutCommand(Command):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.receiver.get_selection()
        self.receiver.delete_selection()


class PasteCommand(Command):
    def execute(self):
        if not self.app.clipboard:
            return
        self.save_backup()
        self.receiver.write(self.app.clipboard)


class UndoCommand(Command):
    def execute(self):
        if len(self.app.history) == 0:
            return
        undo_command = self.app.history.pop()
        undo_command.undo()
