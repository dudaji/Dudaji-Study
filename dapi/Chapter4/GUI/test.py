import unittest
from button.htmlbutton import HtmlButton

class GUITest(unittest.TestCase):
    def test_html_button_creation(self):
        button = HtmlButton()
        self.assertIsNotNone(button, "button is not None")
    
    def test_html_button_render(self):
        button = HtmlButton()
        returnvalue = button.render()
        self.assertEqual(returnvalue, "<button>HTML Button</button>")


if __name__ == '__main__':
    unittest.main()