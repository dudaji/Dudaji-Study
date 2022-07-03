import platform
from factory.macos_factory import MacOSFactory
from factory.linux_factory import LinuxFactory


class Viewer:
    def __init__(self):
        os = platform.system()
        if os not in ("Darwin", "Linux"):
            print(os, "is not supported")
            return
        self.__factory = MacOSFactory() if os == "Darwin" else LinuxFactory()
        self.__button = None
        self.__checkbox = None

    def create_button(self):
        if self.__button:
            print("A button already exists")
            return
        self.__button = self.__factory.create_button()

    def create_checkbox(self):
        if self.__checkbox:
            print("A checkbox already exists")
            return
        self.__checkbox = self.__factory.create_checkbox()

    def render_button(self):
        if self.__button:
            return self.__button.render()
        return ""

    def render_checkbox(self):
        if self.__checkbox:
            return self.__checkbox.render()
        return ""

    def render_all(self):
        return self.render_button() + "\n" + self.render_checkbox()

    def check_checkbox(self):
        if self.__checkbox:
            self.__checkbox.on_check()

    def click_button(self):
        if self.__button:
            return self.__button.on_click()
        return ""
