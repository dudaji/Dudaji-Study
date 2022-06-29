from abc import ABC, abstractmethod
from button.Button import Button

class Dialog(ABC):
    @abstractmethod
    def createButton(self) -> Button:
        pass
    
    def render(self) -> str:
        button = self.createButton()
        button_ui = button.render()
        dialog_name = type(self).__name__
        dash_length = int((36 - len(dialog_name))/2)
        
        space_length = int((34 - len(button_ui))/2)
        return ("-"*dash_length
                + dialog_name
                + "-"*dash_length
                + ("-" if len(dialog_name) % 2 == 1 else "")
                + "\n"
                + "|                                  |\n"
                + "|" 
                + " "*space_length 
                + button_ui 
                + " "*space_length 
                + (" " if len(button_ui) % 2 == 1 else "")
                + "|\n"
                + "|                                  |\n"
                + "------------------------------------\n" + button.onClick())