from checkbox.checkbox import CheckBox


class LinuxCheckBox(CheckBox):
    def render(self):
        checkbox_name = "LinuxCheckBox"
        if self._is_checked:
            return checkbox_name + ":Checked"
        else:
            return checkbox_name + ":NotChecked"
