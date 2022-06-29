from HtmlButton import HtmlButton
from Button import Button
from Dialog import Dialog

class HtmlDialog(Dialog):

    def createButton(self, text: str, padding: int = 0) -> Button:
        return HtmlButton(text, padding)
