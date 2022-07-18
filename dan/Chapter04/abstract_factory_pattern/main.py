from factory import MacOSFactory, WindowsFactory

if __name__ == "__main__":
    print("#" * 30)
    print("type os you want")
    print("1: MacOS")
    print("etc: Windows")
    os = input()
    print("#" * 30)

    print("type button name")
    name = input()
    print("#" * 30)

    print("select checkbox status(1: checked, etc: unchecked)")
    checked = input()
    print("#" * 30, "\n")

    checked = bool(checked == "1")
    if os == "1":
        fac = MacOSFactory()
    else:
        fac = WindowsFactory()

    button = fac.create_button(name)
    checkbox = fac.create_checkbox(checked)

    button.paint()
    checkbox.paint()

    button.click_button()
    checkbox.swiching()
