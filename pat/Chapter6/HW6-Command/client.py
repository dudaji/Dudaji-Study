from Editor import Editor
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    editor = Editor()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
