import enum


class Color32:
    # Idk how to use bytes in python so int's it is
    def __init__(self, r: int, g: int, b: int, a: int = 255) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

        self.Tuple = self.toTuple()
    
    def __str__(self) -> str:
        return f"Color (32-Bit): R:{self.r} G:{self.g} B:{self.b}"
    
    def toTuple(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)
    


class COLOR(enumerate):
    BLACK = Color32(0, 0, 0)
    LIGHT_GRAY = Color32(64, 64, 64)
    RED = Color32(255, 0, 0)
    GREEN = Color32(0, 255, 0)
    BLUE = Color32(0, 0, 255)
    WHITE = Color32(255, 255, 255)
    GRAY = Color32(127, 127, 127)