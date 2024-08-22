class LevelConstructor:
    def __init__(self):
        self.map = [
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        ",
            "                                        "
        ]
        self.starting_bad_spawn = 5
        self.starting_good_spawn = 5
        self.bad_spawn_on_good_collection = 1
        self.good_spawn_on_bad_collection = 1
        self.score_to_win = 5
        self.score_to_lose = -3

    def update_player_based_on_score(self, player):
        if player.last_object == 'G':
            player.manage_temporary_conditions('speed', player.default_speed, 0)
            if player.air_jumps < 1:
                player.air_jumps += 1
        if player.last_object == 'B':
            player.air_jumps = 0
            player.manage_temporary_conditions('speed', 5, 5)
        
        player.last_object = None
        return player