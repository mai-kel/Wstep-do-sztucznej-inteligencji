import numpy as np
import gymnasium as gym
import random

# Actions
# left - zero
# down - one
# right - two
# up - three

class QLearn:
    def __init__(self, is_slippery) -> None:
        self.environment = gym.make("FrozenLake-v1", render_mode=None, is_slippery=is_slippery)
        self.environment.reset()
        self.qtable = np.zeros((self.environment.observation_space.n, self.environment.action_space.n))
        self.is_slippery = is_slippery

    def train(self, alpha, gamma, epsilon, epsilon_decay, episodes, alternative_reward):
        winrates = []
        won_games = 0
        for i in range(episodes):
            state = self.environment.reset()[0]
            is_terminal_state = False
            action = None
            while not is_terminal_state:
                random_num = np.random.random()
                # we choose random action if number is lesser that epsilon
                if random_num < epsilon:
                    action = self.environment.action_space.sample()
                else:
                    if sum(self.qtable[state] != 0):
                        action = np.argmax(self.qtable[state])
                    else:
                        action = self.environment.action_space.sample()

                # we apply chosen action and get new_state, reward and is_terminal_state
                new_state, reward, is_terminal_state = self.environment.step(action)[:3]

                # if chosen, we update reward so it was correct with alternative policy
                if alternative_reward:
                    reward = self.get_alternative_reward(reward, is_terminal_state)

                # if agnet reached target, we increment won_games
                if reward > 0 and is_terminal_state:
                    won_games += 1

                # we update qtable
                self.qtable[state][action] = self.qtable[state][action] + \
                                            alpha * (reward + gamma * np.max(self.qtable[new_state]) - self.qtable[state, action])
                # we update state
                state = new_state

            # we update epsilon
            epsilon -= epsilon*epsilon_decay

            # we add winrate to list of winrates
            winrates.append(won_games/(i+1))

        return winrates

    def get_alternative_reward(self, reward, is_terminal_state):
        if is_terminal_state:
            if reward>0:
                return 10
            else:
                return -2
        else:
            return -0.2


    def play_and_show(self):
        temp_enviroment = gym.make("FrozenLake-v1", render_mode="human", is_slippery=self.is_slippery)
        state = temp_enviroment.reset()[0]
        is_terminal_state = False
        action = None
        while not is_terminal_state:
            action = np.argmax(self.qtable[state])
            new_state, reward, is_terminal_state = temp_enviroment.step(action)[:3]
            state = new_state


    def get_winrate(self, n):
        won_games = 0
        temp_enviroment = gym.make("FrozenLake-v1", render_mode=None, is_slippery=self.is_slippery)
        action = None
        for _ in range(n):
            state = temp_enviroment.reset()[0]
            is_terminal_state = False
            while not is_terminal_state:
                action = np.argmax(self.qtable[state])
                new_state, reward, is_terminal_state = temp_enviroment.step(action)[:3]
                state = new_state
                if (reward > 0 and is_terminal_state):
                    won_games+=1
        return won_games/n


