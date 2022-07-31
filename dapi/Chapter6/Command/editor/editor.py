class Editor:
    def __init__(self):
        self.text = ""
        self.cursor = 0
        self.selected = 0

    def write(self, new_text):
        self.text = self.text[:self.cursor] + new_text + self.text[self.cursor:]

    def get_selection(self, length=0):
        if self.selected == 0 and length == 0:
            return ""
        elif self.selected == 0 or (self.selected != length and length != 0):
            if not length:
                raise ValueError()
            if length not in range(1, len(self.text)):
                raise IndexError()
            self.selected = length
        return self.text[self.cursor:self.cursor+self.selected]

    def delete_selection(self):
        if self.selected == 0:
            return
        self.text = self.text[:self.cursor] + self.text[self.cursor+self.selected:]
        self.selected = 0

    def replace_selection(self, new_text):
        if new_text is None:
            return
        if self.selected == 0:
            return
        self.text = self.text[:self.cursor] + new_text + self.text[self.cursor+self.selected:]
        self.selected = 0

    def move_cursor(self, index):
        if index == -1:
            self.cursor = len(self.text)
            return
        if index not in range(0, len(self.text)):
            raise IndexError()
        self.cursor = index
