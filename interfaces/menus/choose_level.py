import pygame
from game.level_selector import LevelSelector
from game.images import load_images
from interfaces.elements.button import Button
from game.settings import SCREEN_WIDTH, TILE_SIZE, WHITE, RED, BLACK, GRAY, font

buttons = []
easy_button = Button(
    text= "Fácil", 
    value = 'easy',
    x= 40, 
    y= 160, 
    width= 200, 
    height= TILE_SIZE*2, 
    color= BLACK, 
    font=font
)

medium_button = Button(
    text= "Médio", 
    value = 'medium',
    x= 280, 
    y= 160, 
    width= 200, 
    height= TILE_SIZE*2, 
    color= BLACK, 
    font=font
)

hard_button = Button(
    text= "Difícil", 
    value = 'hard',
    x= 520, 
    y= 160, 
    width= 200, 
    height= TILE_SIZE*2, 
    color= BLACK, 
    font=font
)

ultrahard_button = Button(
    text= "Ultra Difícil", 
    value = 'ultrahard',
    x= 760, 
    y= 160, 
    width= 200, 
    height= TILE_SIZE*2, 
    color= BLACK, 
    font=font
)

tutorial_button = Button(
    text= "Tutorial", 
    value = 'tutorial',
    x= 40, 
    y= 40, 
    width= 200, 
    height= TILE_SIZE*2, 
    color= BLACK, 
    font=font
)

def choose_level(screen):
    screen.fill(WHITE)

    images = load_images()
    background_img = images['background1_dark']
    screen.blit(background_img, (0, 0))

    difficulty = None
    level = None
    reload_buttons(screen)

    while not difficulty or not level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.rect.collidepoint(event.pos):
                    difficulty = easy_button.value
                if medium_button.rect.collidepoint(event.pos):
                    difficulty = medium_button.value
                if hard_button.rect.collidepoint(event.pos):
                    difficulty = hard_button.value
                if ultrahard_button.rect.collidepoint(event.pos):
                    difficulty = ultrahard_button.value
                if tutorial_button.rect.collidepoint(event.pos):
                    return tutorial_button.value, 'tutorial'
                reload_buttons(screen, difficulty)
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        level = button.value

        pygame.display.update()
        pygame.time.Clock().tick(30)

    return difficulty, level

def reload_buttons(screen, difficulty=None):
    if difficulty is not None:
        if difficulty == 'easy':
            easy_button.color = GRAY
            medium_button.color = BLACK
            hard_button.color = BLACK
            ultrahard_button.color = BLACK
        if difficulty == 'medium':
            easy_button.color = BLACK
            medium_button.color = GRAY
            hard_button.color = BLACK
            ultrahard_button.color = BLACK
        if difficulty == 'hard':
            easy_button.color = BLACK
            medium_button.color = BLACK
            hard_button.color = GRAY
            ultrahard_button.color = BLACK
        if difficulty == 'ultrahard':
            easy_button.color = BLACK
            medium_button.color = BLACK
            hard_button.color = BLACK
            ultrahard_button.color = GRAY
    else:
        easy_button.color = BLACK
        medium_button.color = BLACK
        hard_button.color = BLACK
        ultrahard_button.color = BLACK


    easy_button.draw(screen)
    medium_button.draw(screen)
    hard_button.draw(screen)
    ultrahard_button.draw(screen)
    tutorial_button.draw(screen)

    # Levels
    if difficulty is not None:
        buttons.clear()
        margin = 40
        button_width = 200
        x_pos=margin
        y_pos = 240

        levels = LevelSelector.level_mapper[difficulty]
        level_names = [name for name in list(levels.keys())]

        for name in level_names:
            button = Button(
                text=name, 
                value = name,
                x= x_pos, 
                y= y_pos, 
                width= button_width, 
                height= TILE_SIZE*2, 
                color= BLACK, 
                font=font
            )

            button.draw(screen)
            buttons.append(button)

            x_pos += button_width + margin