from utilties._v2 import v2 

class sub_tile:
    def __init__(self, world_pos: v2, size: tuple[int, int], parent: object) -> None:
        self.pos = world_pos
        self.size = size
        self.parent_tile = parent

    def alternative_pos(self) -> v2:
        return v2(self.pos.x - (self.size[0]/2), self.pos.y - (self.size[1]/2))
