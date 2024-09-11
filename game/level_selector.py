from levels.levele1 import LevelE1
from levels.levelm1 import LevelM1
from levels.tutorial import TutorialLevel
from levels.levelh1 import LevelH1
from levels.leveluh1 import LevelUH1

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
        'hard': {
            'level1' : LevelH1()
        },

        'ultrahard': {
            'level1' : LevelUH1()
        }
    }

    @staticmethod
    def select(difficulty, level_name):
        return LevelSelector.level_mapper.get(difficulty).get(level_name)
