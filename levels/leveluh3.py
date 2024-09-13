from levels.level_constructor import LevelConstructor
class LevelUH3(LevelConstructor):
    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "                 X                      ",
            " X                                 XX   ",
            "                                        ",
            " XX                    X                ",
            "                             X          ",
            "                                        ",
            "      X              X                  ",
            "                                        ",
            "XXX          XX                      XXX",
            "                           X            ",
            "                                        ",
            "            X                           ",
            " X                    X                 ",
            "                                        ",
            "     X X      XXX       X               ",
            "                                        ",
            "                                        ",
            " X   X      X         X        X       X",
            "                                        ",
            "                                        ",
            "           XX        XX               XX",
            "    X                         X         ",
            "                                        ",
            "X              X        X              X",
            "                                        "
        ]
        self.starting_bad_spawn = 15
        self.starting_good_spawn = 7
        self.bad_spawn_on_good_collection = 3
        self.good_spawn_on_bad_collection = 1
        self.score_to_win = 5
        self.score_to_lose = -3
        self.max_quantity_spawn = sum(line.count('X') for line in self.map)
        self.background = 'background1'