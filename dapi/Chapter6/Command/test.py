import unittest
from editor.editor import Editor


class App:
    def __init__(self, editor:Editor):
        self.editor = editor
        self.clipboard = ""
        self.command_list = {}
    
    def insert_command(self, shortcut, command):
        self.command_list[shortcut] = command(self.editor, self)
    
    def execute_command(self, shortcut):
        self.command_list[shortcut].execute()
    
    def write_editor_text(self, new_text):
        self.editor.write(new_text)
    
    def select_editor_text(self, start, length):
        return self.editor.get_selection(start, length)
    
    def move_editor_cursor(self, index):
        self.editor.move_cursor(index)
        
class CopyCommand:
    def __init__(self, receiver:Editor, app:App):
        self.receiver = receiver
        self.app = app

    def execute(self):
        self.app.clipboard = self.receiver.get_selection()

class CutCommand:
    def __init__(self, receiver:Editor, app:App):
        self.receiver = receiver
        self.app = app

    def execute(self):
        self.app.clipboard = self.receiver.get_selection()
        self.receiver.delete_selection()

class CommandTest(unittest.TestCase):
    def test_editor_write_text(self):
        editor = Editor()
        editor.write("hello")
        self.assertEqual(editor.text, "hello")
        editor.write(" world")
        self.assertEqual(editor.text, "hello world")
    
    def test_editor_get_selection(self):
        editor = Editor()
        editor.write("hello world")
        with self.assertRaises(ValueError):
            editor.get_selection(None, None)
        with self.assertRaises(IndexError):
            editor.get_selection(0, 0)
            editor.get_selection(-1, 4)
            editor.get_selection(17, 1)
            editor.get_selection(0, 17)
        self.assertEqual(editor.get_selection(0, 5), "hello")
        self.assertEqual(editor.get_selection(0, 6), "hello ")
        self.assertEqual(editor.get_selection(), "hello ")
    
    def test_editor_delete_selection(self):
        editor = Editor()
        editor.write("hello world")
        editor.get_selection(0, 5)
        editor.delete_selection()
        self.assertEqual(editor.text, " world")

    def test_editor_replace_selection(self):
        editor = Editor()
        editor.write("hello world")
        editor.get_selection(0, 5)
        editor.replace_selection("bye")
        self.assertEqual(editor.text, "bye world")
        editor.get_selection(0, 3)
        editor.replace_selection("")
        self.assertEqual(editor.text, " world")
        editor.get_selection(0, 1)
        editor.replace_selection(None)
        self.assertEqual(editor.text, " world")
    
    def test_app_insert_command(self):
        editor = Editor()
        app = App(editor)
        app.insert_command("Ctrl+C", CopyCommand)
        self.assertEqual(app.command_list["Ctrl+C"].receiver, editor)
    
    def test_app_execute_command(self):
        editor = Editor()
        app = App(editor)
        app.insert_command("Ctrl+C", CopyCommand)
        app.write_editor_text("hello world")
        self.assertEqual(app.select_editor_text(0, 5), "hello")
        app.execute_command("Ctrl+C")
        self.assertEqual(app.clipboard, "hello")
    
    def test_copy_command_execute(self):
        editor = Editor()
        editor.write("hello world")
        app = App(editor)
        app.select_editor_text(0, 5)
        command = CopyCommand(editor, app)
        command.execute()
        self.assertEqual(app.clipboard, "hello")
    
    def test_cut_command_execute(self):
        editor = Editor()
        editor.write("hello world")
        app = App(editor)
        app.select_editor_text(0, 5)
        command = CutCommand(editor, app)
        command.execute()
        self.assertEqual(app.clipboard, "hello")
        self.assertEqual(editor.text, " world")
    
    def test_cut_command_execute(self):
        editor = Editor()
        editor.write("hello world")
        app = App(editor)
        app.select_editor_text(0, 5)
        copy_command = CopyCommand(editor, app)
        copy_command.execute()
        command = PasteCommand(editor, app)
        command.execute()
        self.assertEqual(app.clipboard, "hello")
        self.assertEqual(editor.text, " world")


if __name__ == "__main__":
    unittest.main()