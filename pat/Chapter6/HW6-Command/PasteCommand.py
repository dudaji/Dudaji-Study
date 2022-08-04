from Command import Command


class PasteCommand(Command):
    def execute(self):
        if self.editor.clipboard == "":
            return False

        self.backup()
        self.editor.textedit.textCursor().insertText(self.editor.clipboard)
        return True
