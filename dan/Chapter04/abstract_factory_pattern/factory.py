import abc


class Button(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def click_button(self) -> None:
        print(self.name, "버튼이 클릭되었습니다.")
        self.paint()

    @abc.abstractmethod
    def paint(self) -> None:
        pass


class MacOSButton(Button):
    def paint(self) -> None:
        print("-" * 30)
        print("MacOS 버튼, name: ", self.name)
        print("-" * 30, "\n")


class WindowsButton(Button):
    def paint(self) -> None:
        print("-" * 30)
        print("Windows 버튼, name: ", self.name)
        print("-" * 30, "\n")


class Checkbox(abc.ABC):
    def __init__(self, checked: bool) -> None:
        self.checked = checked

    def swiching(self) -> None:
        self.checked = not self.checked
        self.paint()

    @abc.abstractmethod
    def paint(self) -> None:
        pass


class WindowsCheckbox(Checkbox):
    def paint(self) -> None:
        print("-" * 30)
        print("Windows Checkbox")
        if self.checked:
            print("☑")
        else:
            print("□")
        print("-" * 30, "\n")


class MacOSCheckbox(Checkbox):
    def paint(self) -> None:
        print("-" * 30)
        print("MacOS Checkbox")
        if self.checked:
            print("☑")
        else:
            print("□")
        print("-" * 30, "\n")


class GUIFactory(abc.ABC):
    @abc.abstractmethod
    def create_button(self, name: str) -> Button:
        pass

    @abc.abstractmethod
    def create_checkbox(self, checked: bool) -> Checkbox:
        pass


class MacOSFactory(GUIFactory):
    def create_button(self, name: str) -> Button:
        return MacOSButton(name)

    def create_checkbox(self, checked: bool) -> Checkbox:
        return MacOSCheckbox(checked)


class WindowsFactory(GUIFactory):
    def create_button(self, name: str) -> Button:
        return WindowsButton(name)

    def create_checkbox(self, checked: bool) -> Checkbox:
        return WindowsCheckbox(checked)
