class Editor:
    def __init__(self):
        self.text = ""
        self.cursor = 0
        self.selected = (None, None)
    # TODO: selected를 cursor를 사용해서 바꾸기

    def write(self, new_text):
        self.text = self.text + new_text
    
    def get_selection(self, start=None, length=None):
        if self.selected != (start, length) and (start, length) != (None, None):
            if start not in range(0, len(self.text)):
                raise IndexError()
            if length not in range(1, len(self.text)):
                raise IndexError()
            self.selected = (start, length)
        if self.selected == (None, None):
            raise ValueError()
        selected_start, selected_length = self.selected
        return self.text[selected_start:selected_start+selected_length]
    
    def delete_selection(self):
        if self.selected == (None, None):
            return
        start, length = self.selected
        self.text = self.text[:start] + self.text[start+length:]
        self.selected = (None, None)
    
    def replace_selection(self, new_text):
        if new_text is None:
            return
        if self.selected == (None, None):
            return
        start, length = self.selected
        self.text = self.text[:start] + new_text + self.text[start+length:]
        self.selected = (None, None)
    
    def move_cursor(self, index):
        self.cursor = index