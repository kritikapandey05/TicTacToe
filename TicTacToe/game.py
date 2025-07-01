### File: game.py

import pygame
import os
import json

LINE_COLOR = (0, 255, 255)
CROSS_COLOR = (255, 80, 80)
CIRCLE_COLOR = (100, 200, 255)
WIN_LINE_COLOR = (255, 255, 100)

pygame.mixer.init()

class Game:
    def __init__(self, screen, font, size):
        self.screen = screen
        self.font = font
        self.size = size
        self.board = [[0]*3 for _ in range(3)]
        self.player = 1
        self.game_over = False
        self.stats_file = "assets/stats.json"
        self.stats = self.load_stats()
        self.sounds = {
            'win': pygame.mixer.Sound("assets/win.mp3"),
            'lose': pygame.mixer.Sound("assets/lose.mp3"),
            'draw': pygame.mixer.Sound("assets/draw.mp3")
        }

    def draw_lines(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * self.size), (self.size*3, i * self.size), 5)
            pygame.draw.line(self.screen, LINE_COLOR, (i * self.size, 0), (i * self.size, self.size*3), 5)

    def draw_symbols(self):
        for row in range(3):
            for col in range(3):
                center = (col * self.size + self.size//2, row * self.size + self.size//2)
                if self.board[row][col] == 1:
                    pygame.draw.line(self.screen, CROSS_COLOR,
                                     (center[0] - 40, center[1] - 40),
                                     (center[0] + 40, center[1] + 40), 8)
                    pygame.draw.line(self.screen, CROSS_COLOR,
                                     (center[0] + 40, center[1] - 40),
                                     (center[0] - 40, center[1] + 40), 8)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, center, 40, 8)

    def draw_score(self):
        score_text = f"You: {self.stats['X']}  AI: {self.stats['O']}  Draws: {self.stats['Draw']}"
        text = self.font.render(score_text, True, (255, 255, 255))
        self.screen.blit(text, (20, 620))

    def draw_result(self, winner):
        msg = f"You Win!" if winner == 1 else ("AI Wins!" if winner == 2 else "Draw!")
        text = self.font.render(msg + " Press R to Restart", True, (255, 255, 0))
        self.screen.blit(text, (40, 650))

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.draw_lines()
        self.draw_symbols()
        self.draw_score()
        if self.game_over:
            self.draw_result(self.check_win())

    def handle_player_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.player
            if self.check_win() or self.is_draw():
                self.end_game()
            else:
                self.player = 2

    def make_ai_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = 2
            if self.check_win() or self.is_draw():
                self.end_game()
            else:
                self.player = 1

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        return 0

    def is_draw(self):
        return all(cell != 0 for row in self.board for cell in row)

    def end_game(self):
        winner = self.check_win()
        if winner:
            self.stats['X' if winner == 1 else 'O'] += 1
            if winner == 1:
                self.sounds['win'].play()
            else:
                self.sounds['lose'].play()
        else:
            self.stats['Draw'] += 1
            self.sounds['draw'].play()
        self.save_stats()
        self.game_over = True

    def reset(self):
        self.board = [[0]*3 for _ in range(3)]
        self.player = 1
        self.game_over = False

    def load_stats(self):
        if os.path.exists(self.stats_file):
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        return {'X': 0, 'O': 0, 'Draw': 0}

    def save_stats(self):
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f)