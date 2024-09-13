from levels.levele1 import LevelE1
from levels.levele2 import LevelE2
from levels.levele3 import LevelE3
from levels.levele4 import LevelE4

from levels.levelm1 import LevelM1
from levels.levelm2 import LevelM2
from levels.levelm3 import LevelM3

from levels.levelh1 import LevelH1
from levels.levelh2 import LevelH2
from levels.levelh3 import LevelH3
from levels.levelh4 import LevelH4

import copy
from levels.tutorial import TutorialLevel
from levels.leveluh1 import LevelUH1
from levels.leveluh2 import LevelUH2
from levels.leveluh3 import LevelUH3
from levels.leveluh4 import LevelUH4


class LevelSelector:
    level_mapper = {
        
        'tutorial': {
            'tutorial': TutorialLevel()
        },
        'easy': {
            'Nivel 1': LevelE1(),
            'Nivel 2': LevelE2(),
            'Nivel 3': LevelE3(),
            'Nivel 4': LevelE4()
        },
        'medium': {
            'Nivel 1': LevelM1(),
            'Nivel 2': LevelM2(),
            'Nivel 3': LevelM3()
        },
        'hard': {
            'Nivel 1' : LevelH1(),
            'Nivel 2' : LevelH2(),
            'Nivel 3' : LevelH3(),
            'Nivel 4' : LevelH4(),
        },

        'ultrahard': {
            'Nivel 1': LevelUH1(),
            'Nivel 2': LevelUH2(),
            'Nivel 3': LevelUH3(),
            'Nivel 4': LevelUH4(),
        }
    }

    @staticmethod
    def select(difficulty, level_name):
        return copy.deepcopy(LevelSelector.level_mapper.get(difficulty).get(level_name))
