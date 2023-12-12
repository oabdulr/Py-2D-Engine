import pygame 
from utilties._v2 import v2 
from utilties._colors import COLOR

from core.map._tile import tile
from core._camera import camera

class debug:
    def __init__(self, pygame: pygame, screen: pygame.surface, cam: camera, resolution: tuple[int, int], tile: tuple[int, int], sub_tile: tuple[int, int]) -> None:
        self.screen = screen
        self.resolution = resolution
        self.tile = tile
        self.sub_tile = sub_tile
        self.cam = cam

        self.pygame = pygame


    def draw_grid_lines(self, sub_grid: bool):
        X = self.resolution[0]
        Y = self.resolution[1]

        tile_x = self.tile[0]
        tile_y = self.tile[1]

        sub_tile_x = self.sub_tile[0]
        sub_tile_y = self.sub_tile[1]


        # sub tiles
        if sub_grid:
            for idx in range((int)(X / sub_tile_x) + 1):
                self.pygame.draw.line(self.screen, COLOR.RED.Tuple, ((idx * sub_tile_x), 0), ((idx * sub_tile_x), Y))

            for idx in range((int)(Y / sub_tile_y) + 1):
                self.pygame.draw.line(self.screen, COLOR.RED.Tuple, (0, (idx * sub_tile_y)), (X, (idx * sub_tile_y)))


        # tiles
        for idx in range((int)(X / tile_x) + 1):
            self.pygame.draw.line(self.screen, COLOR.BLACK.Tuple, ((idx * tile_x), 0), ((idx * tile_x), Y))



        for idx in range((int)(Y / tile_y) + 1):
            self.pygame.draw.line(self.screen, COLOR.BLACK.Tuple, (0, (idx * tile_y)), (X, (idx * tile_y)))


    def draw_tile_lines(self, tiles: list[tile], sub_grid: bool = True):
        font = pygame.font.Font('freesansbold.ttf', 10)
 
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('t', True, COLOR.BLACK.Tuple)
        
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        
        # set the center of the rectangular object.
        for large_tile in tiles:
            if not large_tile.in_view(self.cam):
                continue

            print(large_tile.pos, self.cam.get_position(), self.cam.rad_view, large_tile.pos.distance(self.cam.get_position()))
            #break

            text = font.render(f"({large_tile.id.x}, {large_tile.id.y})", True, COLOR.BLACK.Tuple)
            textRect.center = large_tile.pos.tuple
            textRect.center = (textRect.center[0] - (textRect.width/2), textRect.center[1])
            self.screen.blit(text, textRect)
            self.pygame.draw.rect(self.screen, COLOR.BLACK.Tuple, [large_tile.alternative_pos().x, large_tile.alternative_pos().y, large_tile.size[0], large_tile.size[1]], 1)
            break