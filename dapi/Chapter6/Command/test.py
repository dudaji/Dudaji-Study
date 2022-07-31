import unittest
from editor.editor import Editor
from command.command import CopyCommand, CutCommand, PasteCommand, UndoCommand
from application.app import App


class CommandTest(unittest.TestCase):
    def test_editor_move_cursor(self):
        editor = Editor()
        editor.write("hello world")
        editor.move_cursor(2)
        self.assertEqual(editor.cursor, 2)
        with self.assertRaises(IndexError):
            editor.move_cursor(17)

    def test_editor_write_text(self):
        editor = Editor()
        editor.write("hello")
        self.assertEqual(editor.text, "hello")
        editor.move_cursor(-1)
        editor.write(" world")
        self.assertEqual(editor.text, "hello world")

    def test_editor_get_selection(self):
        editor = Editor()
        editor.write("hello world")
        with self.assertRaises(ValueError):
            editor.get_selection(None)
            editor.get_selection(0)
        with self.assertRaises(IndexError):
            editor.get_selection(17)
        self.assertEqual(editor.get_selection(5), "hello")
        self.assertEqual(editor.get_selection(6), "hello ")
        self.assertEqual(editor.get_selection(), "hello ")
    
    def test_editor_delete_selection(self):
        editor = Editor()
        editor.write("hello world")
        editor.get_selection(5)
        editor.delete_selection()
        self.assertEqual(editor.text, " world")

    def test_editor_replace_selection(self):
        editor = Editor()
        editor.write("hello world")
        editor.get_selection(5)
        editor.replace_selection("bye")
        self.assertEqual(editor.text, "bye world")
        editor.get_selection(3)
        editor.replace_selection("")
        self.assertEqual(editor.text, " world")
        editor.get_selection(1)
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
        self.assertEqual(app.select_editor_text(5), "hello")
        app.execute_command("Ctrl+C")
        self.assertEqual(app.clipboard, "hello")
    
    def test_copy_command_execute(self):
        editor = Editor()
        editor.write("hello world")
        app = App(editor)
        app.select_editor_text(5)
        command = CopyCommand(editor, app)
        command.execute()
        self.assertEqual(app.clipboard, "hello")
    
    def test_cut_command_execute(self):
        editor = Editor()
        editor.write("hello world")
        app = App(editor)
        app.select_editor_text(5)
        command = CutCommand(editor, app)
        command.execute()
        self.assertEqual(app.clipboard, "hello")
        self.assertEqual(editor.text, " world")
    
    def test_paste_command_execute(self):
        editor = Editor()
        editor.write("hello world")
        app = App(editor)
        paste_command = PasteCommand(editor, app)
        copy_command = CopyCommand(editor, app)
        app.select_editor_text(5)
        paste_command.execute()
        self.assertEqual(app.clipboard, "")
        self.assertEqual(editor.text, "hello world")
        copy_command.execute()
        app.move_editor_cursor(-1)
        paste_command.execute()
        self.assertEqual(app.clipboard, "hello")
        self.assertEqual(editor.text, "hello worldhello")
    
    def test_app_save_history(self):
        editor = Editor()
        app = App(editor)
        app.insert_command("Ctrl+C", CopyCommand)
        app.write_editor_text("hello world")
        app.select_editor_text(5)
        app.execute_command("Ctrl+C")
        self.assertEqual(app.clipboard, "hello")
        self.assertEqual(app.history[-1], app.command_list["Ctrl+C"])
    
    def test_command_backup_undo(self):
        editor = Editor()
        editor.write("hello world")
        app = App(editor)
        app.select_editor_text(5)
        command = CutCommand(editor, app)
        command.save_backup()
        self.assertEqual(command.backup, "hello world")
        command.execute()
        self.assertEqual(app.clipboard, "hello")
        self.assertEqual(editor.text, " world")
        command.undo()
        self.assertEqual(editor.text, "hello world")
    
    def test_undo_command_execute(self):
        editor = Editor()
        editor.write("hello world")
        app = App(editor)
        app.select_editor_text(5)
        app.insert_command("Ctrl+X", CutCommand)
        app.insert_command("Ctrl+Z", UndoCommand)
        app.execute_command("Ctrl+X")
        self.assertEqual(app.clipboard, "hello")
        self.assertEqual(editor.text, " world")
        app.execute_command("Ctrl+Z")
        self.assertEqual(editor.text, "hello world")


if __name__ == "__main__":
    unittest.main()