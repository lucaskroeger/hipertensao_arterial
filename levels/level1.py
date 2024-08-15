class Level1:
    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "XXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXX",
            "                                        ",
            "                                        ",
            "XXX  XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "                                        ",
            "                                        ",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XX",
            "                                        ",
            "                                        ",
            "XX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "                                        ",
            "                                        ",
            "XXXX X                                  ",
            "                 XXXX                   ",
            "                                        ",
            "X       X                               ",
            "                                        ",
            "             XXXXXX                     ",
            "                                        ",
            "                        XXXXXX          ",
            "                                        ",
            "                                XXXXX   ",
            "                                        ",
            "         XXXXXXXXXXXXXXXXXXXX           ",
            "                                        ",
            "                                        "
        ]
        self.starting_bad_spawn = 5
        self.starting_good_spawn = 5
        self.bad_spawn_on_good_collection = 3
        self.good_spawn_on_bad_collection = 1
        self.score_to_win = 5
        self.score_to_lose = -3