from WindowsButton import WindowsButton
from Button import Button
from Dialog import Dialog

class WindowsDialog(Dialog):

    def createButton(self, text: str, padding: int = 0) -> Button:
        return WindowsButton(text, padding)
