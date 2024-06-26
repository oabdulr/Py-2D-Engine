from typing import Any
import math


class v2:

    __slots__ = ["x", "y"]
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

   def __iter__():
       yield self.x
       yield self.y

    def set(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def set(self, list: object) -> None:
        self.x = list[0]
        self.y = list[1]
    
    def __add__(self, other):
        return v2(self.x + other.x, self.y + other.y)
    

    def __str__(self) -> str:
        return f"X: {self.x} Y: {self.y}"

    def __eq__(self, __value: object) -> bool:
        if type(__value) == type(self):
            return self.x == __value.x and self.y == __value.y
        return self.x == __value[0] and self.y == __value[1]
    

    def distance(self, __value: object) -> float:
        if type(__value) == type(self):
            return math.sqrt(math.pow(self.x - __value.x, 2) + math.pow((self.y - __value.y), 2))
        return math.sqrt(math.pow(self.x - __value[0], 2) + math.pow((self.y - __value[1]), 2))
