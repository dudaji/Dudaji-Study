import abc

class Command(abc.ABC):
    _editor = None
    _backup = None

    def __init__(self, editor):
        self._editor = editor

    def backup(self) -> None:
        self._backup = self._editor.textField.get()

    def undo(self) -> None:
        self._editor.textField.insert(0, self._backup)

    @abc.abstractmethod
    def execute(self) -> bool:
        pass

class CopyCommand(Command):
    def execute(self) -> bool:
        self._editor.clipboard = self._editor.textField.get()
        return False


class PasteCommand(Command):
    def execute(self) -> bool:
        if not self._editor.clipboard:
            return False
        self.backup()
        self._editor.textField.insert(
            len(self._editor.textField.get()),
            self._editor.clipboard,
        )
        return True


class CutCommand(Command):
    def execute(self) -> bool:
        if not self._editor.textField.get():
            return False

        self.backup()
        source = self._editor.textField.get()
        self._editor.clipboard = source
        self._editor.textField.delete(0, len(source))
        return True
