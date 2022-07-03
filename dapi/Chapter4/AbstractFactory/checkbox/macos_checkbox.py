from checkbox.checkbox import CheckBox


class MacOSCheckBox(CheckBox):
    def render(self):
        checkbox_name = "MacOSCheckBox"
        if self._is_checked:
            return checkbox_name + ":Checked"
        else:
            return checkbox_name + ":NotChecked"
