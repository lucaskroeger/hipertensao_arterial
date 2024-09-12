import pygame
import sys
import random 
from game.images import load_images
from game.player import Player
from game.phase import Phase
from game.level_selector import LevelSelector
from interfaces.menus.end_game import end_game
from interfaces.menus.choose_level import choose_level
from interfaces.elements.screen import create_screen
from game.settings import RED

# Initialize Pygame
pygame.init()

screen = create_screen()

# Initialize Images
images = load_images()

level = None
main_loop = True
replay = False
difficulty = None
level_name = None
while main_loop:
    # Select level
    if not replay:
        difficulty = None
        level_name = None
        difficulty, level_name = choose_level(screen)
    if level is not None:
        del level
    level = LevelSelector.select(difficulty, level_name)

    player = Player(images['player3_rigth'], images['player3_left'])
    phase = Phase(player, level, screen, f'{difficulty}-{level_name}')

    running = True

    while running:
        completed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move()
        player.manageCollision(phase)
        player = level.update_player_based_on_score(player)
        player.manage_temporary_conditions() 
        phase.update()

        if player.score >= level.score_to_win:
            running = False
            end_message = 'Parabéns! Você ganhou!'
        if player.score <= level.score_to_lose:
            running = False
            end_message = 'Não foi dessa vez. Você perdeu!'

    action = end_game(phase, end_message)

    if action == 'quit':
        main_loop = False
    if action == 'replay':
        replay = True
    if action == 'choose_level':
        replay = False
