from utilties._v2 import v2 

class player():
    def __init__(self, health: int = 100, name: str = "UNIDENTIFIED") -> None:
        self.name = name

        self.__health = health
        self.__position = v2(0, 0)

        self.facing = v2(0, 0)

    def update_pos(self, pos: v2) -> None:
        self.__position = pos

    def update_pos_rel(self, pos: v2) -> None:
        self.__position = (self.__position.x + pos.x, self.__position.y + pos.y)

    def set_Health(self, value) -> None:
        self.__health = value

    def get_Health(self) -> int:
        return self.__health
    



