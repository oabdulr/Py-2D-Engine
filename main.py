from utilties._colors import Color32, COLOR
from utilties._v2 import v2 

from core.map._tile import tile
from core.map._generation import generation
from core._player import player
from core._networked_player import networked_player 
from core._camera import camera


from debug._debug import debug

import pygame, time

RESOLUTION = (800, 600)

LARGE_TILE = (40, 40)
SUB_TILE = (10, 10)

WORLD_SIZE = (10000, 10000)

DEBUGING = True


class PG_Display:
    def __init__(self) -> None:
        pygame.init()
        
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()

        self.networked_players = []
        self.tiles = []
        self.camera = camera(600)
        self.world_gen = generation(self.tiles, LARGE_TILE, SUB_TILE, WORLD_SIZE)

        self.running = True

        self.networked_players.append(player(name="local"))

        if DEBUGING:
            gen_time = time.time()
        
        self.world_gen.generate()

        if DEBUGING:
            print(f"**world gen done, elapsed time: {(time.time() - gen_time) * 1000:.2f} ms**")

        if DEBUGING:
            print("DEBUGGING MODE")
            self.debugging = debug(pygame, self.screen, self.camera, RESOLUTION, LARGE_TILE, SUB_TILE)

        self.run()

    
    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        
        movement = v2(0, 0)
        if (pygame.key.get_pressed()[pygame.K_w]):
            movement += v2(0, 10)
        if (pygame.key.get_pressed()[pygame.K_s]):
            movement += v2(0, -10)
        if (pygame.key.get_pressed()[pygame.K_a]):
            movement += v2(10, 0)
        if (pygame.key.get_pressed()[pygame.K_d]):
            movement += v2(-10, 0)
        
        

    def clear_screen(self, color = COLOR.GRAY.Tuple):
        self.screen.fill(COLOR.GRAY.Tuple)

    def render_players(self):
        for player in self.networked_players:
            pygame.draw.circle(self.screen, COLOR.GREEN.Tuple, self.camera.get_position(), 2)
            #pygame.draw.line(self.screen, COLOR.BLACK.Tuple, self.camera.get_position(), self.camera.get_position() + )

    def render_tiles(self):
        for tile in self.tiles:
            pass
            


    def run(self):
        while self.running:
            self.event_check()
            self.clear_screen()
            
            
            self.debugging.draw_tile_lines(self.tiles, sub_grid = False)

            
            

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


PG_Display()