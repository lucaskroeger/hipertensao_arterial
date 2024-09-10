import pygame
from game.settings import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT
from datetime import datetime, timedelta

class Player:
    def __init__(self, image):
        self.name = 'default'
        self.image = image
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.default_speed = 13
        self.speed = 13
        self.default_jump_power = 16
        self.jump_power = 16
        self.gravity = 1.3
        self.default_gravity = 1.3
        self.fast_fall_speed = 7
        self.score = 0
        self.vel_y = 0
        self.is_jumping = False
        self.on_ground = False
        self.jump_key_pressed = False
        self.air_jumps = 0
        self.temporary_conditions = {
            'slowness': None,
            'jump_power': None,
            'gravity': None
        }
        self.x = 50
        self.y = SCREEN_HEIGHT - self.height - TILE_SIZE
        self.rect = pygame.Rect(50, SCREEN_HEIGHT - PLAYER_HEIGHT - TILE_SIZE, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.last_object = None
        self.first_input = None

    def move(self):
        keys = pygame.key.get_pressed()
        if self.first_input is None and (
                            keys[pygame.K_a] 
                            or keys[pygame.K_d]
                            or keys[pygame.K_w] 
                            or keys[pygame.K_s] 
                            or keys[pygame.K_SPACE]):
            self.first_input = datetime.now()

        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            if not self.jump_key_pressed:
                self.jump_key_pressed = True
                if not self.is_jumping:
                    self.vel_y = -self.jump_power
                elif self.air_jumps > 0:
                    self.vel_y = -self.jump_power
                    self.is_jumping = True
                    self.air_jumps -= 1
        else:
            if self.jump_key_pressed:
                self.jump_key_pressed = False
        if keys[pygame.K_s]:
            self.vel_y += self.fast_fall_speed  # Increase falling speed when 'S' is pressed

        # Prevent player to do a jump in the air when falling
        if self.vel_y + self.gravity < self.y:
            self.is_jumping = True

        # Apply gravity
        self.vel_y += self.gravity
        self.y += self.vel_y

        # Prevent the player from going out of bounds
        if self.x < 0:
            self.x = 0
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
        if self.y < 0:
            self.y = 0
            self.vel_y = 0
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            self.vel_y = 0
            self.is_jumping = False
    
    def manageCollision(self, phase):
        
        self.on_ground = False
        self.rect.x = self.x
        self.rect.y = self.y
        
        for row_index, row in enumerate(phase.level.map):
            
            for col_index, tile_code in enumerate(row):
               
                if tile_code in ['X', 'G', 'B']:
                    tile = phase.create_tile(col_index, row_index, tile_code)
                    
                    if tile_code == 'X':
                    
                        if self.rect.colliderect(tile):
                    
                            if self.vel_y >= 0: 
                    
                                if self.y + self.height - self.vel_y <= tile.y:
                                    self.y = tile.y - self.height
                                    self.vel_y = 0
                                    self.is_jumping = False
                                    self.on_ground = True
                    
                            elif self.vel_y < 0: 
                    
                                if self.y >= tile.y + TILE_SIZE:
                                    self.y = tile.y + TILE_SIZE
                                    self.vel_y = 0
                    
                    elif tile_code == 'G' and self.rect.colliderect(tile):                       
                        self.score += 1

                        self.last_object = 'G'
                       
                        phase.create_object_on_random_pos('B', phase.level.bad_spawn_on_good_collection)                    
                        phase.remove_element(col_index, row_index -1)                             
                        phase.level.map[row_index] = phase.level.map[row_index][:col_index] + ' ' + phase.level.map[row_index][col_index + 1:]                    

                    elif tile_code == 'B' and self.rect.colliderect(tile):                    
                        self.score -= 1
                        
                        self.last_object = 'B'
                        
                        phase.create_object_on_random_pos('G', phase.level.good_spawn_on_bad_collection)
                        phase.level.map[row_index] = phase.level.map[row_index][:col_index] + ' ' + phase.level.map[row_index][col_index + 1:]
                        phase.remove_element(col_index, row_index -1)         

    def manage_temporary_conditions(self, condition=None, new_value=None, seconds=None):
        now = datetime.now()
        if condition is not None and new_value is not None and seconds is not None:
            end_time = now + timedelta(seconds=seconds)
            if condition == 'slowness':
                self.speed = new_value
                self.temporary_conditions['slowness'] = end_time
        
        for k, v in list(self.temporary_conditions.items()):
            if v is not None and v <= now:
                print(f'Condition {k} is met. Removing from list. {now}')
                del self.temporary_conditions[k]
                self.speed = self.default_speed

