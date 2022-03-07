class MyClass:
    def __init__(self):
        self._my_dict = {"a": 123, "b": True}

    def set_c(self, value):
        self._my_dict["c"] = value

    def get_c(self):
        return self._my_dict["c"]

    def get_dict_with_twice_a(self):
        buffer = self._my_dict
        buffer["a"] *= 2
        return buffer