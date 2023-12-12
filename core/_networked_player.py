from typing import Any
from core._player import player
from utilties._v2 import v2

class networked_player(player):
    def __init__(self, health: int = 100, name: str = "UNIDENTIFIED") -> None:
        super().__init__(health, name)


