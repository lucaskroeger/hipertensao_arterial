from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, BLACK, WHITE, RED, YELLOW, font, big_font
from datetime import datetime
from interfaces.elements.button import Button
import pygame
from game.score.score_service import ScoreService
from game.score.score import Score

def end_game(phase, message):
    register_score(phase)

    phase.screen.fill(WHITE)

    background_img = phase.images[phase.level.background+'_dark']
    message_text = big_font.render(message, True, WHITE)
    print(len(message))
    print((SCREEN_WIDTH - 25*len(message))/2)
    # Render Time
    time_text  = font.render(f"Tempo: {phase.time}", True, WHITE)

    phase.screen.blit(background_img, (0, 0)) 
    phase.screen.blit(message_text, ((SCREEN_WIDTH - message_text.get_width())/2, 130))
    phase.screen.blit(time_text, ((SCREEN_WIDTH - time_text.get_width())/2, 180))
    
    replay_button = Button(
        text= "Jogar novamente", 
        value = 'replay',
        x= 375, 
        y= 330, 
        width= 250, 
        height= TILE_SIZE*2, 
        color= BLACK, 
        font=font
    )
    choose_level_button = Button(
        text= "Escolher Nível", 
        value = 'choose_level',
        x= 375, 
        y= 390, 
        width= 250, 
        height= TILE_SIZE*2, 
        color= BLACK, 
        font=font
    )
    quit_button = Button(
        text= "Sair", 
        value = 'quit',
        x= 375, 
        y= 450, 
        width= 250, 
        height= TILE_SIZE*2, 
        color= RED, 
        font=font
    )

    replay_button.draw(phase.screen)
    choose_level_button.draw(phase.screen)
    quit_button.draw(phase.screen)

    render_scores(phase)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.rect.collidepoint(event.pos):
                    return replay_button.value
                if choose_level_button.rect.collidepoint(event.pos):
                    return choose_level_button.value
                if quit_button.rect.collidepoint(event.pos):
                    return quit_button.value
                

        pygame.display.flip()
        pygame.time.Clock().tick(30)


def register_score(phase):
    
    if phase.player.score >= phase.level.score_to_win:

        scoreService = ScoreService(phase.level_name)
        
        scoreService.register(Score(phase.player.name, phase.time))
    
def render_scores(phase):
    score_service = ScoreService(phase.level_name)
    scores = score_service.get_top_scores()
    for i in range(len(scores)):
        if str(phase.time) == scores[i]:
            text = font.render(f'{i+1 if i==9 else '  '+str(i+1)}: {scores[i]}', True, YELLOW) 
        else:
            text = font.render(f'{i+1 if i==9 else '  '+str(i+1)}: {scores[i]}', True, WHITE)
        phase.screen.blit(text, (50, 330 + i*30))
