from HtmlDialog import HtmlDialog
# from WindowsDialog import WindowsDialog

def main():
    dialog1 = HtmlDialog('Dialog1', 'Hello, Dudaji!')
    # dialog2 = WindowsDialog('Dialog2')

    dialog1.renderWindow()
    # dialog2.renderWindow()

if __name__ == '__main__':
    main()
