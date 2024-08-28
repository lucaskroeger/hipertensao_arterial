import pygame
import sys
import random 
from game.images import load_images
from game.player import Player
from game.phase import Phase
from game.level_selector import LevelSelector
from game.menus import end_phase

# Initialize Pygame
pygame.init()

# Initialize Images
images = load_images()

# Initialize Player
player = Player(images['player3'])

# Select level
level = LevelSelector.select('medium', 'level1')

# Initialize phase
phase = Phase(player, level)

## Main game loop
running = True

while running:
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
        end_message = 'Ganhou'
    if player.score <= level.score_to_lose:
        running = False
        end_message = 'Perdeu'

end_phase(phase, end_message)
