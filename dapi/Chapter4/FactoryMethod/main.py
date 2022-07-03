from dialog.HtmlDialog import HtmlDialog
from dialog.WindowDialog import WindowDialog

if __name__ == "__main__":
    while True:
        print("Select Dialog")
        print("1 - Html")
        print("2 - Window")
        dialog_type = input()

        if dialog_type == "1" or dialog_type == "2":
            break
        print("Please Select Number 1 or 2")

    if dialog_type == "1":
        new_dialog = HtmlDialog()
    elif dialog_type == "2":
        new_dialog = WindowDialog()

    print(new_dialog.render())
