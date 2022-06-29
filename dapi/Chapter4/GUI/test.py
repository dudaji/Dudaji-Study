import unittest
from button.HtmlButton import HtmlButton
from button.WindowButton import WindowButton
from button.Button import Button
from dialog.HtmlDialog import HtmlDialog
from dialog.WindowDialog import WindowDialog
from dialog.Dialog import Dialog

class GUITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html_button = HtmlButton()
        cls.window_button = WindowButton()
        cls.window_dialog = WindowDialog()
        cls.html_dialog = HtmlDialog()
        print("setUpClass is called")

    def test_abstract_class_button_not_created(self):
        print("Check Button Instance not Created")
        with self.assertRaises(TypeError):
            button = Button()
            print(type(button))
    
    def test_abstract_class_dialog_not_created(self):
        print("Check Dialog Instance not Created")
        with self.assertRaises(TypeError):
            dialog = Dialog()
            print(type(dialog))

    def test_html_button_render(self):
        print("Check HtmlButton render method")
        self.assertEqual(self.html_button.render(
        ), "<button>HTML Button</button>", "html_button rendering is wrong")

    def test_html_button_onClick(self):
        print("Check HtmlButton onClick method")
        self.assertEqual(self.html_button.onClick(),
                         "HTML Button is clicked!", "html_button is not clicked")

    def test_window_button_render(self):
        print("Check WindowButton render method")
        self.assertEqual(self.window_button.render(), "Window Button",
                         "window_button rendering is wrong")

    def test_window_button_onClick(self):
        print("Check WindowButton onClick method")
        self.assertEqual(self.window_button.onClick(),
                         "Window Button is clicked!", "window_button is not clicked")

    def test_window_dialog_createButton(self):
        print("Check WindowDialog createButton method")
        self.assertIsInstance(self.window_dialog.createButton(), WindowButton)

    def test_window_dialog_render(self):
        print("Check WindowDialog render method")
        self.assertEqual(self.window_dialog.render(), ("------------WindowDialog------------\n"
                                                        + "|                                  |\n"
                                                        + "|          Window Button           |\n"
                                                        + "|                                  |\n"
                                                        + "------------------------------------\n" 
                                                        + self.window_button.onClick()))
    
    def test_html_dialog_createButton(self):
        print("Check HtmlDialog createButton method")
        self.assertIsInstance(self.html_dialog.createButton(), HtmlButton)

    
    def test_html_dialog_render(self):
        print("Check HtmlDialog render method")
        self.assertEqual(self.html_dialog.render(), ("-------------HtmlDialog-------------\n"
                                                       + "|                                  |\n"
                                                       + "|   <button>HTML Button</button>   |\n"
                                                       + "|                                  |\n"
                                                       + "------------------------------------\n" 
                                                       + self.html_button.onClick()))
    

if __name__ == '__main__':
    unittest.main()