from copy import deepcopy
from random import choice

class Node:
    def __init__(self, val: 'TicTacToe') -> None:
        self.children = []
        self.val = val
        self.rating = None

    def get_children(self) -> list:
        return self.children

    def add_children(self, child: 'Node'):
        self.children.append(child)


class TicTacToe:
    def __init__(self, turn: str, size) -> None:
        self.board = [[' ' for j in range(size)] for i in range(size)]
        self.turn = turn
        self.is_ended = False
        self.winner = None
        self.size = size

    def _check_if_ended(self):
        # player X won
        if self._did_player_win('X'):
            self.is_ended = True
            self.winner = 'X'

        # player 0 won
        elif self._did_player_win('O'):
            self.is_ended = True
            self.winner = 'O'

        # draw
        else:
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == ' ':
                        return
            self.is_ended = True

    def _did_player_win(self, player: str) -> bool:
        """
        Method checks if given player has won the game

        Parameters:
        player (str): player's mark, can be whether 'X' or 'O'
        """
        # checking vertically
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != player:
                    break
                else:
                    counter += 1
            if counter == self.size:
                return True
            else:
                counter = 0

        # checking horizontally
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[j][i] != player:
                    break
                else:
                    counter += 1
            if counter == self.size:
                return True
            else:
                counter = 0

        # checking diagonally from top-left to bottom-right
        counter = 0
        for i in range(self.size):
            if self.board[i][i] != player:
                break
            else:
                counter += 1
        if counter == self.size:
            return True

        # checking diagonally from top-left to bottom-right
        counter = 0
        for i in range(self.size):
            if self.board[(self.size - 1) - i][i] != player:
                break
            else:
                counter += 1
        if counter == self.size:
            return True

        return False

    def apply_move(self, column, row):
        self.board[column][row] = self.turn
        self.turn = 'X' if self.turn == 'O' else 'O'
        self._check_if_ended()

    @staticmethod
    def print_board(game: 'TicTacToe'):
        for i in range(game.size):
            print('-'*(4*game.size + 1))
            row = ""
            row += "|"
            for j in range(game.size):
                row += f' {game.board[j][i]} '
                row += "|"
            print(row)
        print('-'*(4*game.size + 1))


class Minimax:
    def __init__(self, turn, size) -> None:
        # X - max
        # O - mini
        self.size = size
        self.turn = turn
        self.root = self._make_game_tree(self.size)
        pass

    def _make_game_tree(self, board_size: int):
        game = TicTacToe(self.turn, self.size)
        root = Node(game)
        self._make_game_tree_rec(board_size, root)
        return root

    def _make_game_tree_rec(self, board_size: int, node: Node):
        moves = self._get_all_possible_moves(node.val)
        for move in moves:
            val = deepcopy(node.val)
            val.apply_move(move[0], move[1])
            child = Node(val)
            node.add_children(child)
            self._make_game_tree_rec(board_size, child)

        if node.children:
            node.rating = max(node.children, key=lambda x: x.rating).rating \
                if node.val.turn == 'X' else min(node.children, key=lambda x: x.rating).rating
        else:
            if node.val.winner == 'X':
                node.rating = 1
            elif node.val.winner == 'O':
                node.rating = -1
            else:
                node.rating = 0

    def _get_all_possible_moves(self, game: TicTacToe):
        moves = []
        if game.is_ended:
            return moves
        for i in range(game.size):
            for j in range(game.size):
                if game.board[i][j] == " ":
                    moves.append((i, j))
        return moves

    def play(self, minimax):
        game_history = []
        current_node = self.root
        while not current_node.val.is_ended:
            if current_node.val.turn == 'X':
                if minimax == 'X':
                    not_losing_children = [child for child in current_node.children if child.rating != -1]
                    current_node = choice(not_losing_children)
                else:
                    current_node = choice([child for child in current_node.children])
            else:
                if minimax == 'O':
                    not_losing_children = [child for child in current_node.children if child.rating != 1]
                    current_node = choice(not_losing_children)
                else:
                    current_node = choice([child for child in current_node.children])
            game_history.append(current_node.val)
        return game_history

    @staticmethod
    def print_history_game(game_history):
        for game_state in game_history:
            TicTacToe.print_board(game_state)


class Data_analyzer:
    def __init__(self) -> None:
        pass

    def get_minimax_winrate(self, n, who_begins, who_minimax, size):
        minimax = Minimax(who_begins, size)
        minimax_won_games = 0
        for i in range(n):
            minimax_won_games += 1 if minimax.play(who_minimax)[-1].winner == who_minimax else 0
        return minimax_won_games/n
