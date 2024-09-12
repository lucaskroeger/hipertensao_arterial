from levels.level_constructor import LevelConstructor
class TutorialLevel(LevelConstructor):
    def __init__(self):
        super().__init__()
        self.map = [
            "                                        ",
            "                                        ",
            "                 XXXX  XXXXX            ",
            "           X                            ",
            "                                        ",
            "                X                       ",
            "                      X                 ",
            "                         XXXXXXXXXX     ",
            "                                        ",
            "                                        ",
            "             XXXXXXXXXXXX               ",
            "                                        ",
            "                                        ",
            "       XXXXX                  XXXXXXXX  ",
            "                                        ",
            "                                        ",
            "     XXX          XXX      XXX        XX",
            "                                        ",
            "                                        ",
            "XX       XXXXXXXX     XXXXXXXXX    XXXXX",
            "                                        ",
            "                                        ",
            "      XX                                ",
            "                            X           ",
            "         XXXXXXXXXXXX                   ",
            "    X                                   ",
            "                                        ",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ]
        self.starting_bad_spawn = 5
        self.starting_good_spawn = 5
        self.bad_spawn_on_good_collection = 1
        self.good_spawn_on_bad_collection = 1
        self.score_to_win = 5
        self.score_to_lose = -3
        self.background = 'backgroundTu'
        self.max_quantity_spawn = sum(line.count('X') for line in self.map)

     
    
   