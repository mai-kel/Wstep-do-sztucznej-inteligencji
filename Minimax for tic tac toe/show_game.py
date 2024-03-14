import argparse
from tic_tac_toe import Minimax

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('who_begins', type=str)
    parser.add_argument('who_minimax', type=str)
    args = parser.parse_args()

    who_begins = str(args.who_begins).upper()
    who_minimax = str(args.who_minimax).upper()

    minimax = Minimax(who_begins, 3)
    Minimax.print_history_game(minimax.play(who_minimax))

