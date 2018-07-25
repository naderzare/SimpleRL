import config
import copy
class Game:
    def __init__(self):
        self.finished = False
        self.player_pos = [0, 0]
        self.step = 0
        self.board = []
        for x in range(config.game_board_high):
            ys = []
            for y in range(config.game_board_width):
                ys.append('.')
            self.board.append(copy.copy(ys))
        self.board[config.game_goal_pos[0]][config.game_goal_pos[1]] = 'G'
        for h in config.game_holes_pos:
            self.board[h[0]][h[1]] = 'H'
        self.board[self.player_pos[0]][self.player_pos[1]] = 'P'

    def update(self, action):
        self.step += 1
        new_player_pos = copy.copy(self.player_pos)
        if action == 'u' or action == 1:
            new_player_pos[1] -= 1
        if action == 'd' or action == 2:
            new_player_pos[1] += 1
        if action == 'l' or action == 3:
            new_player_pos[0] -= 1
        if action == 'r' or action == 4:
            new_player_pos[0] += 1
        self.board[self.player_pos[0]][self.player_pos[1]] = '.'
        self.player_pos = new_player_pos
        if self.board[new_player_pos[0]][new_player_pos[1]] in ('.', 'P'):
            self.board[new_player_pos[0]][new_player_pos[1]] = 'P'
        return self.get_reward(new_player_pos)

    def get_reward(self, new_player_pos):
        if new_player_pos == config.game_goal_pos:
            self.finished = True
            return config.learning_goal_reward
        if new_player_pos in config.game_holes_pos:
            self.finished = True
            return config.learning_hole_reward
        if new_player_pos[0] < 0 or new_player_pos[0] >= config.game_board_width:
            self.finished = True
            return config.learning_out_reward
        if new_player_pos[1] < 0 or new_player_pos[1] >= config.game_board_width:
            self.finished = True
            return config.learning_out_reward
        if self.step > config.game_max_episode_time:
            self.finished = True
            return config.learning_timeout_reward
        return config.learning_move_reward

    def print_game(self):
        print ('step:{}'.format(self.step))
        for y in range(0,config.game_board_high):
            l = ''
            for x in range(0, config.game_board_width):
                l += self.board[x][y]
            print (l + '\n')


