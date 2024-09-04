from levels.levele1 import LevelE1
from levels.levelm1 import LevelM1
from levels.tutorial import TutorialLevel

class LevelSelector:
    level_mapper = {
        
        'tutorial': {
            'level1': TutorialLevel()
        },
        'easy': {
            'level1': LevelE1()
        },
        'medium': {
            'level1': LevelM1()
        },
        'hard': {},
        'ultrahard': {}
    }

    @staticmethod
    def select(difficulty, level_name):
        return LevelSelector.level_mapper.get(difficulty).get(level_name)
