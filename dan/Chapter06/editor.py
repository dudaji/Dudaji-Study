import tkinter as tk

from command import CopyCommand, CutCommand, PasteCommand
from commandHistory import CommandHistory


class Editor:
    _root = tk
    textField = None
    _history = CommandHistory()

    def create(self):
        self._root = self._root.Tk()
        self.textField = tk.Entry(self._root)
        self._root.title("Text editor")
        content = tk.Label(self._root, text="Type & Use Buttons")
        content.pack()

        self.textField.pack()

        editor = self

        copy_command = CopyCommand(editor)
        cut_command = CutCommand(editor)
        paste_command = PasteCommand(editor)

        ctrl_c = tk.Button(
            self._root,
            text="Ctrl + C",
            command=lambda: self.excuteCommand(copy_command)
        )

        ctrl_x = tk.Button(
            self._root,
            text="Ctrl + X",
            command=lambda: self.excuteCommand(cut_command)
        )
        ctrl_v = tk.Button(
            self._root,
            text="Ctrl + V",
            command=lambda: self.excuteCommand(paste_command)
        )
        ctrl_z = tk.Button(
            self._root,
            text="Ctrl + Z",
            command=lambda: self.undo()
        )

        btns = [ctrl_c, ctrl_x, ctrl_v, ctrl_z]
        for btn in btns:
            btn.pack()

        self._root.mainloop()

    def excuteCommand(self, command):
        if command.execute():
            self._history.push(command)

    def undo(self):
        if self._history.isEmpty():
            return

        command = self._history.pop()
        if command:
            command.undo()
