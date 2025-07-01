import random
import copy

class AI:
    def __init__(self, game, level="hard"):
        self.game = game
        self.level = level

    def make_move(self):
        if self.level == "easy":
            self.random_move()
        elif self.level == "medium":
            self.minimax_move(depth=1)
        else:
            self.minimax_move(depth=3)

    def random_move(self):
        empty = [(r, c) for r in range(3) for c in range(3) if self.game.board[r][c] == 0]
        if empty:
            row, col = random.choice(empty)
            self.game.make_ai_move(row, col)

    def minimax_move(self, depth):
        best_score = -float('inf')
        best_move = None

        for r in range(3):
            for c in range(3):
                if self.game.board[r][c] == 0:
                    temp_board = copy.deepcopy(self.game.board)
                    temp_board[r][c] = 2
                    score = self.minimax(temp_board, depth, False)
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
        if best_move:
            self.game.make_ai_move(*best_move)

    def minimax(self, board, depth, is_maximizing):
        winner = self.fake_check_win(board)
        if winner == 2:
            return 1
        elif winner == 1:
            return -1
        elif all(cell != 0 for row in board for cell in row):
            return 0

        if depth == 0:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = 2
                        score = self.minimax(board, depth - 1, False)
                        board[r][c] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = 1
                        score = self.minimax(board, depth - 1, True)
                        board[r][c] = 0
                        best_score = min(score, best_score)
            return best_score

    def fake_check_win(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != 0:
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != 0:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != 0:
            return board[0][2]
        return 0
