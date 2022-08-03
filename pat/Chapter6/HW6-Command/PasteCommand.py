from Command import Command


def PasteCommand(Command):
    def execute(self):
        if self.editor.clipboard == None or self.editor.clipboard.isEmpty():
            return False

        self.backup()
        self.editor.textField.insert(
            self.editor.clipboard, self.editor.textField.getCaretPosition()
        )
        return True
