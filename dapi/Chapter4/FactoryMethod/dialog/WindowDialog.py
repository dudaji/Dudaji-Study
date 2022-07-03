from dialog.Dialog import Dialog
from button.WindowButton import WindowButton


class WindowDialog(Dialog):
    def createButton(self):
        return WindowButton()
