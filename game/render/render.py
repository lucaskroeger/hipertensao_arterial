from abc import ABC, abstractmethod

class Render(ABC):
        
    @abstractmethod
    def render(self, phase):
        pass