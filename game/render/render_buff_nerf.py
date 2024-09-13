from game.render.render import Render
from game.settings import SCREEN_WIDTH


class RenderBuffNerf(Render):
    
    def __init__(self): 
        self.icon_position = {
            'slowness': [SCREEN_WIDTH - 300,15],
            'jump_power': [SCREEN_WIDTH - 350, 15],
            'gravity': [10, 10]
        }

    def render(self, phase):
        self.handle_condition_icon('slowness', phase) 
        self.handle_condition_icon('jump_power', phase)
    
    def handle_condition_icon(self, condition_str, phase):
        if condition_str in phase.player.temporary_conditions:
            condition = phase.player.temporary_conditions[condition_str]

            if condition is not None:
                self.add_icon(phase.images[condition_str], self.icon_position[condition_str][0],self.icon_position[condition_str][1], phase)        
            elif condition_str == 'jump_power' and phase.player.air_jumps > 0:
                self.add_icon(phase.images[condition_str], self.icon_position[condition_str][0],self.icon_position[condition_str][1], phase)        

    def add_icon(self, image, x, y, phase):
        phase.screen.blit(image, (x, y))         
