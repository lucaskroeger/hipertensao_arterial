from levels.level_constructor import LevelConstructor
class LevelM1(LevelConstructor):
    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "XXXXXX             XXXXXXXXXX           ",
            "                                        ",
            "                                    XXXX",
            "XXXXXX        XXXX                      ",
            "                                        ",
            "                                        ",
            "XXXXXX                         XXX      ",
            "                                        ",
            "                                        ",
            "          XXXXXXXX                  XXXX",
            "                                        ",
            "                                        ",
            "XXXX                   XXXXX            ",
            "                                        ",
            "                                        ",
            "        XXXXXXXX                 XXXXXXX",
            "                                        ",
            "                                        ",
            "                     XXXXXXX            ",
            "                                        ",
            "                                        "
        ]
        self.starting_bad_spawn = 18
        self.starting_good_spawn = 5
        self.bad_spawn_on_good_collection = 1
        self.good_spawn_on_bad_collection = 1
        self.score_to_win = 5
        self.score_to_lose = -3
        self.maxQuantitySpawn = sum(line.count('X') for line in self.map)
        self.background = 'background1'