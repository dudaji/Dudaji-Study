from command import Command

class CommandHistory:
    _history = None

    def __init__(self):
        self._history = []

    def push(self, command) -> None:
        print("hi")
        self._history.push(command)

    def pop(self) -> Command:
        return self._history.pop()

    def isEmpty(self) -> bool:
        return bool(self._history)
