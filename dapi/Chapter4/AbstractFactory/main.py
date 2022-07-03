from viewer import Viewer


def configure_viewer(viewer: Viewer) -> Viewer:
    selection = None
    while selection is None:
        try:
            print("Select")
            print("1 - Button")
            print("2 - Check Box")
            print("3 - Both")
            print("4 - Nothing")
            selection = int(input())
            if selection not in (1, 2, 3, 4):
                raise ValueError()
        except ValueError:
            print("Invalid Input\n")
            selection = None

    if selection == 1:
        viewer.create_button()
        print("A button is created!")
    elif selection == 2:
        viewer.create_checkbox()
        print("A check box is created!")
    elif selection == 3:
        viewer.create_button()
        viewer.create_checkbox()
        print("A button and a check box are created!")
    elif selection == 4:
        print("Nothing is created!")

    return viewer


def print_viewer_ui(viewer: Viewer):
    print("\n---------------Viewer---------------\n")
    print(viewer.render_all())
    print("\n------------------------------------\n")


def run_viewer(viewer: Viewer):
    selection = None
    while selection is None:
        try:
            print("Select")
            print("1 - Click a button")
            print("2 - Check a check box")
            print("3 - Exit viewer")
            selection = int(input())
            if selection not in (1, 2, 3):
                raise ValueError()
        except ValueError:
            print("Invalid Input\n")
            selection = None

        if selection == 2:
            viewer.check_checkbox()
        elif selection == 3:
            break

        print_viewer_ui(viewer)

        if selection == 1:
            print(viewer.click_button() + "\n")

        selection = None


def main():
    viewer = Viewer()
    viewer = configure_viewer(viewer)
    print_viewer_ui(viewer)
    run_viewer(viewer)


if __name__ == "__main__":
    main()
