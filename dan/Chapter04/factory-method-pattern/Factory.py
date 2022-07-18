import abc
import tkinter as tk


class Button(abc.ABC):
    @abc.abstractmethod
    def render(self):
        pass

    @abc.abstractmethod
    def onClick(self):
        pass


class HtmlButton(Button):
    def render(self) -> None:
        print("<button> Test Button </button>")
        self.onClick()

    def onClick(self) -> None:
        print("Click! Button says - 'Hello World!'")


class MacButton(Button):
    root = tk

    def render(self):
        self.root = self.root.Tk()
        txt = tk.Label(self.root, text="Hello World!")
        self.root.geometry("200x100")
        self.root.title("Mac ")
        txt.pack()
        self.onClick()
        self.root.mainloop()

    def onClick(self):
        btn = tk.Button(self.root, text="exit", command=self.root.destroy)
        btn.pack()


class Dialog:
    def renderWindow(self) -> None:
        btn = self.createButton()
        btn.render()

    @abc.abstractmethod
    def createButton(self) -> Button:
        pass


class HtmlDialog(Dialog):
    def createButton(self) -> Button:
        return HtmlButton()


class MacDialog(Dialog):
    def createButton(self) -> Button:
        return MacButton()
