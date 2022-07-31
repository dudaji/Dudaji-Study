from editor.editor import Editor

class App:
    def __init__(self, editor:Editor):
        self.editor = editor
        self.clipboard = ""
        self.command_list = {}
        self.history = []
    
    def insert_command(self, shortcut, command):
        self.command_list[shortcut] = command(self.editor, self)
    
    def execute_command(self, shortcut):
        self.command_list[shortcut].execute()
        self.save_history(self.command_list[shortcut])
    
    def write_editor_text(self, new_text):
        self.editor.write(new_text)
        self.editor.move_cursor(-1)
    
    def select_editor_text(self, length=0):
        return self.editor.get_selection(length)
    
    def move_editor_cursor(self, index):
        self.editor.move_cursor(index)
    
    def save_history(self, command):
        self.history.append(command)