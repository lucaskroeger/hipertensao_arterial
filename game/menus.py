from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, font
from datetime import datetime
import pygame

def end_phase(phase, message):
    phase.screen.fill(WHITE)

    background_map = {
        'background1': 'background1_dark',
        'backgroundTu': 'background1_dark',
    }

    background_key = background_map.get(phase.level.background, phase.level.background + '_dark')

    background_img = phase.images[background_key]

    message_text = font.render(message, True, WHITE)

    # Render Time
    time_text  = font.render(f"Time: {phase.time}", True, WHITE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        phase.screen.blit(background_img, (0, 0)) 
        phase.screen.blit(message_text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        phase.screen.blit(time_text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+30))

        pygame.display.flip()
        pygame.time.Clock().tick(30)


