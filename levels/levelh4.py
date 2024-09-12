from levels.level_constructor import LevelConstructor
class LevelH4(LevelConstructor):
    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       ",
            "                                        ",
            "             X       X                  ",
            "                                        ",
            "                X                       ",
            "                                        ",
            "  XXXXXXXXXXXXXXXX            XXXXXXX   ",
            "                                        ",
            "                                        ",
            "                       XXXXXX           ",
            "                                        ",
            "      XXXXXX                            ",
            "                                        ",
            "                    XXXXXX              ",
            "                                        ",
            "     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ",
            "                                        ",
            "      X       X    X     X       X      ",
            "                                        ",
            "    X      X         X       X          ",
            "                                        ",
            "       XXXXXXX           XXXXXXX        ",
            "  X               X                  X  ",
            "                                        ",
            "X       XXXX          XXXXXX        XXXX",
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