import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, PLAYER_WIDTH, PLAYER_HEIGHT

def load_images():
    images = {
        'background1': pygame.image.load('images/scenario/background1.png'),
        'backgroundTu': pygame.image.load('images/scenario/backgroundTu.png'),
        'background1_dark': pygame.image.load('images/scenario/background1_dark.png'),
        'platform': pygame.image.load('images/scenario/platform.png'),
        'good1': pygame.image.load('images/foods/good/1.png'),
        'good2': pygame.image.load('images/foods/good/2.png'),
        'good3': pygame.image.load('images/foods/good/3.png'),
        'bad1': pygame.image.load('images/foods/bad/1.png'),
        'bad2': pygame.image.load('images/foods/bad/2.png'),
        'player1': pygame.image.load('images/players/1.png'),
        'player2': pygame.image.load('images/players/2.png'),
        'player3': pygame.image.load('images/players/3.png'),
        'player4': pygame.image.load('images/players/4.png')
    }

    # Scale images
    images['background1'] = pygame.transform.scale(images['background1'], (SCREEN_WIDTH, SCREEN_HEIGHT))
    images['backgroundTu'] = pygame.transform.scale(images['backgroundTu'], (SCREEN_WIDTH, SCREEN_HEIGHT))
    images['background1_dark'] = pygame.transform.scale(images['background1_dark'], (SCREEN_WIDTH, SCREEN_HEIGHT))
    images['platform'] = pygame.transform.scale(images['platform'], (TILE_SIZE, TILE_SIZE))
    images['good1'] = pygame.transform.scale(images['good1'], (TILE_SIZE, TILE_SIZE))
    images['good2'] = pygame.transform.scale(images['good2'], (TILE_SIZE, TILE_SIZE))
    images['good3'] = pygame.transform.scale(images['good3'], (TILE_SIZE, TILE_SIZE))
    images['bad1'] = pygame.transform.scale(images['bad1'], (TILE_SIZE, TILE_SIZE))
    images['bad2'] = pygame.transform.scale(images['bad2'], (TILE_SIZE, TILE_SIZE))
    images['player1'] = pygame.transform.scale(images['player1'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player2'] = pygame.transform.scale(images['player2'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player3'] = pygame.transform.scale(images['player3'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player4'] = pygame.transform.scale(images['player4'], (PLAYER_WIDTH, PLAYER_HEIGHT))

    return images
