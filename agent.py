import copy
import config
class Agent:
    def __init__(self):
        self.action_number = 5
        self.Q = []
        for x in range(config.game_board_width):
            xs = []
            for y in range(config.game_board_high):
                acs = []
                for a in range(self.action_number):
                    acs.append(config.learning_first_q)
                xs.append(copy.copy(acs))
            self.Q.append(copy.copy(xs))
    