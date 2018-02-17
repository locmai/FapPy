class MData:
    def __init__(self, value_name, display_name, value=None):
        self.value_name = value_name
        self.display_name = display_name
        self.value = value

    @property
    def get_value_name(self):
        return self.value_name

    @property
    def get_display_name(self):
        return self.display_name
    @property
    def get_value(self):
        return self.value
