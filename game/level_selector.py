from levels.levele1 import LevelE1
from levels.levelm1 import LevelM1
import copy

class LevelSelector:
    level_mapper = {
        'easy': {
            'Nivel 1': LevelE1(),
            'Nivel 2': LevelE1(),
            'Nivel 3': LevelE1(),
            'Nivel 4': LevelE1()
        },
        'medium': {
            'Nivel 1': LevelM1(),
            'Nivel 2': LevelM1(),
            'Nivel 3': LevelM1(),
            'Nivel 4': LevelM1()
        },
        'hard': {},
        'ultrahard': {}
    }

    @staticmethod
    def select(difficulty, level_name):
        return copy.deepcopy(LevelSelector.level_mapper.get(difficulty).get(level_name))
