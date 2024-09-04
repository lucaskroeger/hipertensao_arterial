from game.render.render import Render
from game.render.render_heart import RenderHeart
from game.render.render_time import RenderTime
from game.render.render_buff_nerf import RenderBuffNerf

class RenderFactory:
    
    def __init__(self):
        self.renders = {
            'heart': RenderHeart(),
            'time': RenderTime(),
            'buff-nerf': RenderBuffNerf()
        }
        
    def get_implementation(self, type):
        
        return self.renders[type]
    
