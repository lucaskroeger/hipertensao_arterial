import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

def create_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hipertensão Arterial")
    return screen
