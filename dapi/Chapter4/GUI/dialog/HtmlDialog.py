from dialog.Dialog import Dialog
from button.HtmlButton import HtmlButton

class HtmlDialog(Dialog):
    def createButton(self):
        return HtmlButton()