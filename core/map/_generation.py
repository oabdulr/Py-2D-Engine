from core.map._tile import tile
from core.map._sub_tile import sub_tile
from utilties._v2 import v2 

class generation:
    def __init__(self, tiles: list[tile], large_tile: tuple[int, int], sub_tile: tuple[int, int], size = (1000, 1000)) -> None:
        self.tiles: list[tile]           = tiles
        self.size: tuple[int, int]       = size
        self.large_tile: tuple[int, int] = large_tile
        self.sub_tile: tuple[int, int]   = sub_tile

    
    '''
    "Generates" tiles, it basically does math for where the center point of every tile should bes
    '''
    def generate(self) -> None:
        _sub_tiles = []
        for y_tile in range((int)(self.size[1] / self.large_tile[1])):
            for x_tile in range((int)(self.size[0] / self.large_tile[0])):
                
                center_world = v2(((x_tile+1) * self.large_tile[0]) - self.large_tile[0]/2, ((y_tile+1) * self.large_tile[1]) - self.large_tile[1]/2)
                print(center_world)
                _sub_tiles.clear()
                _tile = tile(center_world, self.large_tile, id=v2(x_tile, y_tile)) 
                for y_sub_tile in range((int)(self.large_tile[1] / self.sub_tile[1])):
                    for x_sub_tile in range((int)(self.large_tile[0] / self.sub_tile[0])):
                        sub_center_world = v2( (((x_tile) * self.large_tile[0])) + ((x_sub_tile+1) * self.sub_tile[0]) - self.sub_tile[0]/2, (((y_tile) * self.large_tile[1])) + ((y_sub_tile+1) * self.sub_tile[1]) - self.sub_tile[1]/2)
                        _sub_tiles.append(sub_tile(sub_center_world, self.sub_tile, _tile))
                _tile.update_subtiles(_sub_tiles)
                self.tiles.append(_tile)



        
