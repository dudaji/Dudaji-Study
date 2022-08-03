from Command import Command


class CopyCommand(Command):
    def execute(self):
        self.editor.clipboard = self.editor.textField.getSelectedText()
        return False
