from game.render.render import Render
from game.render.render_heart import RenderHeart
from game.render.render_time import RenderTime

class RenderFactory:
    
    def __init__(self):
        self.renders = {
            'heart': RenderHeart(),
            'time': RenderTime()
        }
        
    def get_implementation(self, type):
        
        return self.renders[type]
    
