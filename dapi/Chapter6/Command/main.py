from editor.editor import Editor
from command.command import CopyCommand, CutCommand, PasteCommand, UndoCommand
from application.app import App

if __name__ == "__main__":
    editor = Editor()
    app = App(editor)
    app.insert_command("Ctrl+C", CopyCommand)
    app.insert_command("Ctrl+V", PasteCommand)
    app.insert_command("Ctrl+X", CutCommand)
    app.insert_command("Ctrl+Z", UndoCommand)
    
    print("This is Text Editor Application")
    while True:
        try:
            print("----Text----")
            print(app.editor.text)
            print("------------")
            print("cursor: ", app.editor.cursor)
            if app.editor.text != "":
                if app.select_editor_text() != "":
                    print("selected text: ", app.select_editor_text())
                if app.clipboard != "":
                    print("clipboard: ", app.clipboard)
            print("\n")
            
            print("1 - Write Text")
            print("2 - Move Cursor")
            print("3 - Select Text")
            print("4 - Copy Text")
            print("5 - Cut Text")
            print("6 - Paste Text")
            print("7 - Undo (Paste, Cut)")
            print("8 - Exit")
            selection = int(input())
            if selection not in range(1, 9):
                raise ValueError()
        except ValueError:
            print("Invalid Input\n")
            selection = None
            
        
        print("\n----Text----")
        print(app.editor.text)
        print("------------")
        print("cursor: ", app.editor.cursor)
        if app.editor.text != "":
            if app.select_editor_text() != "":
                print("selected text: ", app.select_editor_text())
            if app.clipboard != "":
                print("clipboard: ", app.clipboard)
        print("\n")
        
        if selection == 1:
            print("--Write Text--")
            text = input()
            app.write_editor_text(text)
        elif selection == 2:
            print("--Move Cursor--")
            cursor = int(input())
            app.move_editor_cursor(cursor)
        elif selection == 3:
            print("--Select Text--")
            length = int(input())
            app.select_editor_text(length)
        elif selection == 4:
            print("--Copy Text--")
            app.execute_command("Ctrl+C")
        elif selection == 5:
            print("--Cut Text--")
            app.execute_command("Ctrl+X")
        elif selection == 6:
            print("--Paste Text--")
            app.execute_command("Ctrl+V")
        elif selection == 7:
            print("--Undo--")
            app.execute_command("Ctrl+Z")
        elif selection == 8:
            print("--Exit--")
            break
        print("\n")
