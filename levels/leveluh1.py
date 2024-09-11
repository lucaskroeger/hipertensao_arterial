from levels.level_constructor import LevelConstructor
class LevelUH1(LevelConstructor):
    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "    X             X     X           XX  ",
            "                                        ",
            "          X                             ",
            "                       X                ",
            "XXX                             XXX     ",
            "                                        ",
            "                     X                  ",
            "                                        ",
            "       XXXXXX                    XXXXX  ",
            "                           X            ",
            "                                        ",
            "                                        ",
            "    X                      XXXX         ",
            "                                        ",
            "           XXXXXX       X               ",
            "                                        ",
            "                                        ",
            " X   X        X     X     X      X      ",
            "                                        ",
            "                                        ",
            "           XX        XX          XXXXX  ",
            "                                        ",
            "                                        ",
            "XX X           X        X       X      X",
            "                                        "
        ]
        self.starting_bad_spawn = 5
        self.starting_good_spawn = 5
        self.bad_spawn_on_good_collection = 3
        self.good_spawn_on_bad_collection = 1
        self.score_to_win = 5
        self.score_to_lose = -3
        self.max_quantity_spawn = sum(line.count('X') for line in self.map)
        self.background = 'background1'