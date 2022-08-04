from Command import Command


class CutCommand(Command):
    def execute(self):
        self.cursor = self.editor.textedit.textCursor()
        selectedText = self.editor.textedit.textCursor().selectedText()

        if selectedText == "":
            return False

        self.backup()
        source = self.editor.textedit.toPlainText()
        self.editor.clipboard = selectedText
        self.editor.textedit.setText(self.cutString(source))
        return True

    def cutString(self, source):
        start = source[: self.cursor.selectionStart()]
        end = source[self.cursor.selectionEnd() :]
        return start + end
