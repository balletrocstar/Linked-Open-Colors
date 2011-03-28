
def if_else(condition, trueVal, falseVal):
    """
    A Java-like ternary operator
    """
    if condition:
        return trueVal
    else:
        return falseVal

class KeyInsensitiveDict:
    """
    A simple implementation of a key-insensitive dictionary (implemented by using the pattern decorator).
    Original developed for the Python SPARQL Wrapper: http://www.wikier.org/blog/key-insensitive-dictionary-in-python
    """

    def __init__(self, d={}):
        self.__dict__["d"] = {}
        for k, v in d.items(): self[k] = v

    def __getattr__(self, attr):
        return getattr(self.__dict__["d"], attr)

    def __setattr__(self, attr, value):
        setattr(self.__dict__["d"], attr, value)

    def __setitem__(self, key, value):
        if (hasattr(key, "lower")):
            key = key.lower()
        self.__dict__["d"][key] = value

    def __getitem__(self, key):
        if (hasattr(key, "lower")):
            key = key.lower()
        return self.__dict__["d"][key]

