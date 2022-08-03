from Command import Command


def CutCommand(Command):
    def execute(self):
        if self.editor.textField.getSelectedText().isEmpty():
            return False

        self.backup()
        source = self.editor.textField.getText()
        self.editor.clipboard = self.editor.textField.getSelectedText()
        self.editor.textField.setText(self.cutString(source))
        return True

    def cutString(self, source):
        start = source.substring(0, self.editor.textField.getSelectionStart())
        end = source.substring(self.editor.textField.getSelectionEnd())
        return start + end
