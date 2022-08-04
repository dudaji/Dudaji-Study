from inspect import ismemberdescriptor
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QTextEdit,
)
from functools import partial
from CommandHistory import CommandHistory
from CopyCommand import CopyCommand
from CutCommand import CutCommand
from PasteCommand import PasteCommand


class Editor(QWidget):
    def __init__(self):
        super().__init__()
        self._history = CommandHistory()
        self.clipboard = ""
        self.textedit = QTextEdit()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Editor")
        self.resize(600, 300)
        hbox = QHBoxLayout()
        copyButton = QPushButton("Copy")
        cutButton = QPushButton("Cut")
        pasteButton = QPushButton("Paste")
        undoButton = QPushButton("Undo")

        copyButton.clicked.connect(
            partial(self._executeCommand, CopyCommand(self))
        )
        cutButton.clicked.connect(
            partial(self._executeCommand, CutCommand(self))
        )
        pasteButton.clicked.connect(
            partial(self._executeCommand, PasteCommand(self))
        )
        undoButton.clicked.connect(self._undo)

        buttons = QVBoxLayout()
        buttons.addWidget(copyButton)
        buttons.addWidget(cutButton)
        buttons.addWidget(pasteButton)
        buttons.addWidget(undoButton)

        hbox.addWidget(self.textedit)
        hbox.addLayout(buttons)

        self.setLayout(hbox)
        self.show()

    def _executeCommand(self, cmd):
        if cmd.execute():
            self._history.push(cmd)

    def _undo(self):
        if self._history.isEmpty():
            return
        cmd = self._history.pop()
        if cmd is not None:
            cmd.undo()
