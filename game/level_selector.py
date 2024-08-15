from levels.level1 import Level1

class LevelSelector:
    level_mapper = {
        'easy': {
            'level1': Level1()
        }
    }

    @staticmethod
    def select(difficulty, level_name):
        return LevelSelector.level_mapper.get(difficulty).get(level_name)
