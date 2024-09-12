from game.render.render import Render
from datetime import datetime
from game.settings import SCREEN_WIDTH, WHITE, font


class RenderTime(Render):

    def render(self, phase):
        
        if phase.player.first_input:
            
            now = datetime.now() 

            time_played = now - phase.player.first_input
            total_seconds = int(time_played.total_seconds())
            minutes, seconds = divmod(total_seconds, 60)
            milliseconds = time_played.microseconds // 10000
            phase.time = f"{minutes:02}:{seconds:02}.{milliseconds:02}"

        time_text  = font.render(f"Time: {phase.time}", True, WHITE)
        phase.screen.blit(time_text, (SCREEN_WIDTH-213, 30))