import game

g = game.Game()
g.print_game()
while not g.finished:
    ac = input()
    g.update(ac)
    g.print_game()