from button.linux_button import LinuxButton
from checkbox.linux_checkbox import LinuxCheckBox
from factory.factory import GUIFactory


class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckBox()
