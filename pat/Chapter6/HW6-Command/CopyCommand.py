from Command import Command


class CopyCommand(Command):
    def execute(self):
        cursor = self.editor.textedit.textCursor()
        self.editor.clipboard = self.editor.textedit.textCursor().selectedText()
        return False
