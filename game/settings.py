import pygame

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Tile dimensions
TILE_SIZE = 25

# Player dimensions
PLAYER_HEIGHT = TILE_SIZE * 2
PLAYER_WIDTH = TILE_SIZE

# Font
pygame.font.init()
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (102, 102, 102)
YELLOW = (255, 255, 0)