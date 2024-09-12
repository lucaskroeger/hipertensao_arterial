from levels.levele1 import LevelE1
from levels.levele2 import LevelE2
from levels.levele3 import LevelE3
from levels.levele4 import LevelE4

from levels.levelm1 import LevelM1
from levels.mid.mid_level import MidLevel
from levels.mid.mid_level_1 import MidLevel1

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
            'level1': TutorialLevel()
        },
        'easy': {
            'Nivel 1': LevelE1(),
            'Nivel 2': LevelE2(),
            'Nivel 3': LevelE3(),
            'Nivel 4': LevelE4()
        },
        'medium': {
            'Nivel 1': MidLevel(),
            'Nivel 2': LevelM1(),
            'Nivel 3': MidLevel1()
        },
        'hard': {
            'level1' : LevelH1(),
            'level2' : LevelH2(),
            'level3' : LevelH3(),
            'level4' : LevelH4(),
        },

        'ultrahard': {
            'level1': LevelUH1(),
            'level2': LevelUH2(),
            'level3': LevelUH3(),
            'level4': LevelUH4(),
        }
    }

    @staticmethod
    def select(difficulty, level_name):
        return copy.deepcopy(LevelSelector.level_mapper.get(difficulty).get(level_name))
