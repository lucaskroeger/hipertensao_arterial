from levels.level_constructor import LevelConstructor

class MidLevel1(LevelConstructor):

    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "                                        ",
            "    X                             X     ",
            "                    xx                  ",
            "                                        ",
            "                                        ",
            "    XXX                        XXX      ",
            "                                        ",
            "                                        ",
            "                    XXXXX               ",
            "                                        ",
            "                                        ",
            "       X                      XXXXX     ",
            "                                        ",
            "                                        ",
            "      XXX          XXX                XX",
            "                                        ",
            "                                        ",
            "XX             X             XXX    XXXX",
            "                                        ",
            "                                        ",
            "        XXXX                            ",
            "                                        ",
            "                                        ",
            "                       XXXXXXXX         ",
            "                                        ",
            "                                        "
        ]
        self.starting_bad_spawn = 5
        self.starting_good_spawn = 5
        self.bad_spawn_on_good_collection = 5
        self.good_spawn_on_bad_collection = 2
        self.score_to_win = 6
        self.maxQuantitySpawn = sum(line.count('X') for line in self.map)
        self.score_to_lose = -2
        self.background = 'background1'