from game.render.render import Render

class RenderHeart(Render):
    
    def render(self, phase):
        
        pos_y = 10
        pos_x = 10        
        
        lose = (-phase.level.score_to_lose) 
        total = lose + phase.level.score_to_win
        
        total_hearts = lose + phase.player.score
        total_empty_hearts = total - total_hearts

        for i in range(total_hearts):

            phase.screen.blit(phase.images['heart'], (pos_x, pos_y))         
        
            pos_x += 40

        for i in range(total_empty_hearts):
            
            phase.screen.blit(phase.images['empty-heart'], (pos_x, pos_y))         
        
            pos_x += 40
    