from Command import Command


class PasteCommand(Command):
    def execute(self):
        if self.editor.clipboard is None or self.editor.clipboard.isEmpty():
            return False

        self.backup()
        self.editor.textField.insert(
            self.editor.clipboard, self.editor.textField.getCaretPosition()
        )
        return True
