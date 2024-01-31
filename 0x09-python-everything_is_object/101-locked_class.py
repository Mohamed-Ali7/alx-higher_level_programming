#!/usr/bin/python3
class LockedClass:

    def __setattr__(self, name, value):
        error = f"'{__class__.__name__}' object has no attribute '{name}'"
        if name != "first_name":
            raise AttributeError(error)
        self.__dict__[name] = value
