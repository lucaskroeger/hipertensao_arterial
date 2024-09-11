from levels.levele1 import LevelE1
from levels.levelm1 import LevelM1
<<<<<<< HEAD
from levels.tutorial import TutorialLevel
from levels.levelh1 import LevelH1
=======
from levels.mid.mid_level import MidLevel
>>>>>>> 205a4b6a6f743ee3cdd999dc445dc014d2997a47

class LevelSelector:
    level_mapper = {
        
        'tutorial': {
            'level1': TutorialLevel()
        },
        'easy': {
            'level1': LevelE1()
        },
        'medium': {
            'level1': MidLevel()
        },
        'hard': {
            'level1' : LevelH1
        },

        'ultrahard': {}
    }

    @staticmethod
    def select(difficulty, level_name):
        return LevelSelector.level_mapper.get(difficulty).get(level_name)
