from levels.levele1 import LevelE1
from levels.levelm1 import LevelM1
from levels.mid.mid_level import MidLevel

class LevelSelector:
    level_mapper = {
        'easy': {
            'level1': LevelE1()
        },
        'medium': {
            'level1': MidLevel()
        },
        'hard': {},
        'ultrahard': {}
    }

    @staticmethod
    def select(difficulty, level_name):
        return LevelSelector.level_mapper.get(difficulty).get(level_name)
