from button.macos_button import MacOSButton
from checkbox.macos_checkbox import MacOSCheckBox
from factory.factory import GUIFactory


class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckBox()
