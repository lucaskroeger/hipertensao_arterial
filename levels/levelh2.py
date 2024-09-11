from levels.level_constructor import LevelConstructor
class LevelH1(LevelConstructor):
    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "                          XXXXXXXX      ",
            "        XXXXXXXXX                       ",
            "                                        ",
            "                        XXXXXXXX        ",
            "                                        ",
            "            XXXXX                       ",
            "                                        ",
            "                                        ",
            "        XXXXXXX                         ",
            "                                        ",
            "    XXXXXX                              ",
            "                            XXXXXXXX    ",
            "                                        ",
            "               XXXXXXX                  ",
            "XXXXX                                   ",
            "                                        ",
            "     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ",
            "                                        ",
            "         X    X       X                 ",
            "                                        ",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "                                        ",
            "           X      X        X            ",
            "                                        ",
            "        XXX    XXX   XXX                ",
            "                                        "
        ]
        self.starting_bad_spawn = 5
        self.starting_good_spawn = 5
        self.bad_spawn_on_good_collection = 1
        self.good_spawn_on_bad_collection = 1
        self.score_to_win = 5
        self.score_to_lose = -3
        self.background = 'background1'