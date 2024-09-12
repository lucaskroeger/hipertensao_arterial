import pygame
from game.images import load_images
from game.settings import SCREEN_WIDTH,SCREEN_HEIGHT,TILE_SIZE,WHITE,font
import random 
from game.render.render_factory import RenderFactory

from game.element import Element

class Phase:
    def __init__(self, player, level, screen):
        self.images = load_images()
        self.elements = []
        self.screen = screen
        self.player = player
        self.level = level
        self.score = 0
        self.time = '00:00.00'
        print(level)

        self.create_object_on_random_pos('B', level.starting_bad_spawn)
        self.create_object_on_random_pos('G', level.starting_good_spawn)
        self.update()
        
    def draw_background(self):
        background_img = self.images[self.level.background]
        self.screen.blit(background_img, (0, 0)) 

    def draw_player(self):
        player_img = pygame.Rect(self.player.x, SCREEN_HEIGHT - self.player.height - TILE_SIZE, self.player.width, self.player.height)
        self.screen.blit(self.player.image, (self.player.x, self.player.y))

    def create_tile(self, x_pos, y_pos, tile_type):
        tile_rect = pygame.Rect(x_pos * TILE_SIZE, y_pos * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        if tile_type == 'X':
            self.screen.blit(self.images['platform'], tile_rect.topleft)
        elif tile_type == 'G':
            self.screen.blit(self.get_image(x_pos, y_pos, 'G'), tile_rect.topleft)
        elif tile_type == 'B':
            self.screen.blit(self.get_image(x_pos, y_pos, 'B'), tile_rect.topleft)
        return tile_rect

    def draw_platforms(self):
        for row_index, row in enumerate(self.level.map):  # Draw all tiles
            for col_index, tile_code in enumerate(row):
                if tile_code in ['X', 'G', 'B']:
                    self.create_tile(col_index, row_index, tile_code)

    def create_object_on_random_pos(self, object, quantity):
        for i in range(quantity):
            count_platform = 0
            for row in self.level.map:
                count_platform += row.count('X')
            could_be_placed = False
            tries = 0
            while not could_be_placed:
                tries += 1 
                pos = random.randint(0, count_platform)
                cur_pos = 0
                for row_index, row in enumerate(self.level.map):
                    for col_index, tile_code in enumerate(row):
                        if tile_code == 'X':
                            if cur_pos == pos:
                                if self.level.map[row_index-1][col_index] == ' ' or len(self.elements) >= (self.level.max_quantity_spawn - 10):
                                    self.level.map[row_index-1] = self.level.map[row_index-1][:col_index] + object + self.level.map[row_index-1][col_index + 1:]                                
                                    could_be_placed = True
                            cur_pos += 1

    def render_game_stats(self):
        RenderFactory().get_implementation('heart').render(self)
        RenderFactory().get_implementation('time').render(self)
        RenderFactory().get_implementation('buff-nerf').render(self)

    def update(self):
        self.draw_background()
        self.draw_player()
        self.draw_platforms()
        self.render_game_stats()
        pygame.display.flip()
        pygame.time.Clock().tick(30)

    def get_random_image(self, type):

        if type == 'G':
            
            range = 3

            return self.images['good' + str(random.randint(1, range))]

        elif type == 'B':
            
            range = 2

            return self.images['bad' + str(random.randint(1, range))]

    def get_image(self, x, y, type):

        currentElement = next(filter(lambda element: element.x == x and element.y == y, self.elements), None)

        if currentElement != None:
            return currentElement.image
        else:
            
            image = self.get_random_image(type)
            
            element = Element(x, y, image, type == 'G')
            
            self.elements.append(element)

            return element.image
    
    def remove_element(self, x, y):
        self.elements[:] = [element for element in self.elements if element.x != x and element.y != y]
