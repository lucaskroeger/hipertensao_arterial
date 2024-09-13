from levels.level_constructor import LevelConstructor

class LevelM3(LevelConstructor):

    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "                                        ",
            "    X                             X     ",
            "                                        ",
            "                                        ",
            "                                        ",
            "    XXX     XXXX               XXXX     ",
            "                                        ",
            "                                        ",
            "             XXXXXXXXXXXX               ",
            "                                        ",
            "                                        ",
            "       X               XXX    XXXXX     ",
            "                                        ",
            "                                        ",
            "      XXX          XXX                XX",
            "                                        ",
            "                                        ",
            "XX                          XXX    XXXXX",
            "                                        ",
            "                                        ",
            "        XXXXXXXXXXX                     ",
            "                                        ",
            "                                        ",
            "                       XXXXXXXX         ",
            "                                        ",
            "                                        "
        ]
        self.starting_bad_spawn = 10
        self.starting_good_spawn = 5
        self.bad_spawn_on_good_collection = 1
        self.good_spawn_on_bad_collection = 1
        self.score_to_win = 5
        self.max_quantity_spawn = sum(line.count('X') for line in self.map)
        self.score_to_lose = -3
        self.background = 'background1'