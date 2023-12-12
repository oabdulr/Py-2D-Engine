from utilties._v2 import v2 
from core._camera import camera

class tile:
    def __init__(self, world_pos: v2, size: tuple[int, int], sub_tiles = list([])) -> None:
        self.pos = world_pos
        self.sub_tiles = sub_tiles
        self.size = size

    def alternative_pos(self) -> v2:
        return v2(self.pos.x - (self.size[0]/2), self.pos.y - (self.size[1]/2))

    def update_subtiles(self, tiles: list[object]):
        self.sub_tiles = tiles

    def in_view(self, cam: camera) -> bool:
        return (self.pos.distance(cam.get_position()) < cam.rad_view)
            