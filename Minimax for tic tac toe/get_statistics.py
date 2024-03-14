import argparse
import matplotlib.pyplot as plt
from tic_tac_toe import Data_analyzer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('number_of_games_to_be_analyzed', type=int)
    args = parser.parse_args()
    n = int(args.number_of_games_to_be_analyzed)

    data_analyzer = Data_analyzer()
    labels = ["Minimax starts the game", "Random move gnerator starts the game"]
    winrates = []
    winrates.append(data_analyzer.get_minimax_winrate(n, "X", "X", 3))
    winrates.append(data_analyzer.get_minimax_winrate(n, "O", "X", 3))
    plt.title(f'Minimax winrate in {n} games on 3x3 board')
    plt.ylabel("Winrate")
    plt.bar(labels, winrates)
    plt.show()