class CommandHistory:
    def __init__(self):
        self._history = []
    
    def push(self, cmd):
        self._history.append(cmd)
    
    def pop(self):
        return self._history.pop()
    
    def isEmpty(self):
        return len(self._history) == 0
