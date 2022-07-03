import platform
import unittest

from button.macos_button import MacOSButton
from button.linux_button import LinuxButton
from button.button import Button
from checkbox.macos_checkbox import MacOSCheckBox
from checkbox.linux_checkbox import LinuxCheckBox
from checkbox.checkbox import CheckBox
from factory.macos_factory import MacOSFactory
from factory.linux_factory import LinuxFactory
from factory.factory import GUIFactory
from viewer import Viewer


class CrossPlatformGUITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.macos_button = MacOSButton()
        cls.linux_button = LinuxButton()
        cls.macos_checkbox = MacOSCheckBox()
        cls.linux_checkbox = LinuxCheckBox()
        cls.macos_factory = MacOSFactory()
        cls.linux_factory = LinuxFactory()
        cls.viewer = Viewer()
        print("setUpClass is called")

    def test_macos_button_render(self):
        print("test MacOSButton render method")
        self.assertEqual(self.macos_button.render(), "MacOSButton")

    def test_macos_button_on_click(self):
        print("test MacOSButton on_click method")
        self.assertEqual(self.macos_button.on_click(), "MacOSButton is clicked!")

    def test_linux_button_render(self):
        print("test LinuxButton render method")
        self.assertEqual(self.linux_button.render(), "LinuxButton")

    def test_linux_button_on_click(self):
        print("test LinuxButton on_click method")
        self.assertEqual(self.linux_button.on_click(), "LinuxButton is clicked!")

    def test_button_creation(self):
        print("test Button creation")
        with self.assertRaises(TypeError):
            button = Button()
            print(type(button))

    def test_macos_checkbox_render(self):
        print("test MacOSCheckBox render method")
        self.assertIn(
            self.macos_checkbox.render(),
            ("MacOSCheckBox:NotChecked", "MacOSCheckBox:Checked"),
        )

    def test_macos_checkbox_on_check(self):
        print("test MacOSCheckBox on_check method")
        before = self.macos_checkbox.render()
        self.macos_checkbox.on_check()
        after = self.macos_checkbox.render()
        self.assertTrue(
            after != before
            and after in ("MacOSCheckBox:NotChecked", "MacOSCheckBox:Checked")
        )

    def test_linux_checkbox_render(self):
        print("test LinuxCheckBox render method")
        self.assertIn(
            self.linux_checkbox.render(),
            ("LinuxCheckBox:NotChecked", "LinuxCheckBox:Checked"),
        )

    def test_linux_checkbox_on_check(self):
        print("test LinuxCheckBox on_check method")
        before = self.linux_checkbox.render()
        self.linux_checkbox.on_check()
        after = self.linux_checkbox.render()
        self.assertTrue(
            after != before
            and after in ("LinuxCheckBox:NotChecked", "LinuxCheckBox:Checked")
        )

    def test_checkbox_creation(self):
        print("test CheckBox creation")
        with self.assertRaises(TypeError):
            checkbox = CheckBox()
            print(type(checkbox))

    def test_macos_factory_create_button(self):
        print("test MacOSFactory create_button method")
        button = self.macos_factory.create_button()
        self.assertEqual(button.render(), self.macos_button.render())

    def test_macos_factory_create_checkbox(self):
        print("test MacOSFactory create_checkbox method")
        checkbox = self.macos_factory.create_checkbox()
        self.assertIn(
            checkbox.render(), ("MacOSCheckBox:NotChecked", "MacOSCheckBox:Checked")
        )

    def test_linux_factory_create_button(self):
        print("test LinuxFactory create_button method")
        button = self.linux_factory.create_button()
        self.assertEqual(button.render(), self.linux_button.render())

    def test_linux_factory_create_checkbox(self):
        print("test LinuxFactory create_checkbox method")
        checkbox = self.linux_factory.create_checkbox()
        self.assertIn(
            checkbox.render(), ("LinuxCheckBox:NotChecked", "LinuxCheckBox:Checked")
        )

    def test_factory_creation(self):
        print("test Factory creation")
        with self.assertRaises(TypeError):
            factory = GUIFactory()
            print(type(factory))

    def test_viewer_create_button(self):
        print("test viewer create_button method")
        before = self.viewer.render_button()
        self.viewer.create_button()
        after = self.viewer.render_button()
        self.assertTrue(
            (before != after)
            and (
                after == "MacOSButton"
                if platform.system() == "Darwin"
                else "LinuxButton"
            )
        )

    def test_viewer_create_checkbox(self):
        print("test viewer create_checkbox method")
        before = self.viewer.render_checkbox()
        self.viewer.create_checkbox()
        after = self.viewer.render_checkbox()
        self.assertTrue(
            (before != after)
            and (
                after
                in (
                    ("MacOSCheckBox:NotChecked", "MacOSCheckBox:Checked")
                    if platform.system() == "Darwin"
                    else ("LinuxCheckBox:NotChecked", "LinuxCheckBox:Checked")
                )
            )
        )

    def test_viewer_render_all_components(self):
        print("test viewer render_all method")
        os = platform.system()
        if os == "Darwin":
            button = MacOSButton()
            checkbox = MacOSCheckBox()
        elif os == "Linux":
            button = LinuxButton()
            checkbox = LinuxCheckBox()
        else:
            print("Not supported os")
            return

        viewer = Viewer()
        button = button.render()
        notchecked_checkbox = checkbox.render()
        checkbox.on_check()
        checked_checkbox = checkbox.render()

        self.assertEqual(viewer.render_all(), "\n")
        viewer.create_button()
        self.assertEqual(viewer.render_all(), button + "\n")
        viewer.create_checkbox()
        self.assertEqual(viewer.render_all(), button + "\n" + notchecked_checkbox)

    def test_viewer_click_button(self):
        print("test viewer click button method")
        os = platform.system()
        if os == "Darwin":
            button = MacOSButton()
        elif os == "Linux":
            button = LinuxButton()
        else:
            print("Not supported os")
            return
        viewer = Viewer()
        viewer.create_button()
        self.assertEqual(viewer.click_button(), button.on_click())

    def test_viewer_check_checkbox(self):
        print("test viewer check checkbox method")
        os = platform.system()
        if os == "Darwin":
            checkbox = MacOSCheckBox()
        elif os == "Linux":
            checkbox = LinuxCheckBox()
        else:
            print("Not supported os")
            return

        viewer = Viewer()
        viewer.create_checkbox()
        before = viewer.render_checkbox()
        viewer.check_checkbox()
        after = viewer.render_checkbox()

        self.assertTrue(before == checkbox.render())
        checkbox.on_check()
        self.assertTrue(after == checkbox.render())


if __name__ == "__main__":
    unittest.main()
