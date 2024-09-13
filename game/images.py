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
        'player1_right': pygame.image.load('images/players/1_r.png'),
        'player1_left': pygame.image.load('images/players/1_l.png'),
        'player2_right': pygame.image.load('images/players/2_r.png'),
        'player2_left': pygame.image.load('images/players/2_l.png'),
        'player3_right': pygame.image.load('images/players/3_r.png'),
        'player3_left': pygame.image.load('images/players/3_l.png'),
        'player4_right': pygame.image.load('images/players/4_r.png'),
        'player4_left': pygame.image.load('images/players/4_l.png'),
        'heart': pygame.image.load('images/heart/heart.png'),
        'empty-heart': pygame.image.load('images/heart/empty-heart.png'),
        'slowness': pygame.image.load('images/debuff/debuff-slowness.png'),
        'jump_power': pygame.image.load('images/buffs/buff-jump-power.png')
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
    images['player1_right'] = pygame.transform.scale(images['player1_right'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player1_left'] = pygame.transform.scale(images['player1_left'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player2_right'] = pygame.transform.scale(images['player2_right'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player2_left'] = pygame.transform.scale(images['player2_left'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player3_right'] = pygame.transform.scale(images['player3_right'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player3_left'] = pygame.transform.scale(images['player3_left'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player4_right'] = pygame.transform.scale(images['player4_right'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['player4_left'] = pygame.transform.scale(images['player4_left'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    images['slowness'] = pygame.transform.scale(images['slowness'], (50, 50))
    images['jump_power'] = pygame.transform.scale(images['jump_power'], (50, 50))

    return images
