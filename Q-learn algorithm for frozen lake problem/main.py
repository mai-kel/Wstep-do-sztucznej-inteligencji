from frozen_lake import QLearn
import matplotlib.pyplot as plt
import argparse

def plot_winrates(winrates, title):
    plt.figure()
    plt.plot([i for i in range(len(winrates))], winrates)
    plt.xlabel("Epizod")
    plt.ylabel("Winratio")
    plt.title(title)

if __name__ == '__main__':

    # getting params
    parser = argparse.ArgumentParser()
    parser.add_argument('alpha', type=float, help="Learning rate parameter ranges from 0 to 1")
    parser.add_argument('gamma', type=float, help="Discount factor parameter ranges 0 to 1")
    parser.add_argument('epsilon', type=float, help="Starting epsilon parameter ranges 0 to 1")
    parser.add_argument('epsilon_decay', type=float, help="It determines how fast will epsilon decrease 0 to 1")
    parser.add_argument('episodes', type=int, help="Number of episodes")
    parser.add_argument ('games_to_test', type=int, help="Determines how many games will be studied during measuring winrate")
    args = parser.parse_args()
    alpha = args.alpha
    gamma = args.gamma
    epsilon = args.epsilon
    epsilon_decay = args.epsilon_decay
    episodes = args.episodes
    games_to_test = args.games_to_test

    qleran = QLearn(True)
    default_winrates = qleran.train(alpha, gamma, epsilon, epsilon_decay, episodes, False)
    print(f'Winratio na próbce {games_to_test} gier dla domyślnego systemu nagród: {qleran.get_winrate(games_to_test)*100}%')

    qleran2 = QLearn(True)
    custom_winrates = qleran2.train(alpha, gamma, epsilon, epsilon_decay, episodes, True)
    print(f'Winratio na próbce {games_to_test} gier dla niestandardowego systemu nagród: {qleran2.get_winrate(games_to_test)*100}%')

    plot_winrates(default_winrates, "Winratio w zależności od epizodu dla domyślnego systemu nagród")
    plot_winrates(custom_winrates, "Winratio w zależności od epizodu dla niestandardowego systemu nagród")

    plt.show()


