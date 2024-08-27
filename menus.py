from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, font
from datetime import datetime
import pygame

def end_phase(phase, message):
    phase.screen.fill(WHITE)

    background_img = phase.images[phase.level.background+'_dark']
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


