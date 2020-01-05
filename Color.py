class Color:
    def __init__(self):
        self.h = 0.3
        self.s = 0.3
        self.v = 0.9

    def __str__(self) -> str:
        return str(self.h) + " " + str(self.s) + " " + str(self.v)