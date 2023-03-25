class Boolean:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class TableRow:
    x1 = Boolean()
    x2 = Boolean()
    x3 = Boolean()
    result = Boolean()

    def __init__(self, x1=None, x2=None, x3=None, result=None):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.result = result
