import pygame
import sys
from game import Game
from ai import AI

pygame.init()
WIDTH, HEIGHT = 600, 700
SQUARE_SIZE = WIDTH // 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" AI Tic Tac Toe")
font = pygame.font.Font("assets/PressStart2P.ttf", 20)
clock = pygame.time.Clock()
FPS = 60

# Colors
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)

# Difficulty Selector
level = None

def draw_level_screen():
    screen.fill(BG_COLOR)
    title = font.render("Choose AI Level:", True, TEXT_COLOR)
    easy = font.render("1 - Easy", True, TEXT_COLOR)
    medium = font.render("2 - Medium", True, TEXT_COLOR)
    hard = font.render("3 - Hard", True, TEXT_COLOR)
    screen.blit(title, (50, 200))
    screen.blit(easy, (50, 280))
    screen.blit(medium, (50, 340))
    screen.blit(hard, (50, 400))
    pygame.display.update()

# Wait for level selection
waiting = True
while waiting:
    draw_level_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print("Key pressed:", event.key)
            if event.key == pygame.K_1:
                level = "easy"
                waiting = False
            elif event.key == pygame.K_2:
                level = "medium"
                waiting = False
            elif event.key == pygame.K_3:
                level = "hard"
                waiting = False

# Game init
game = Game(screen, font, SQUARE_SIZE)
ai = AI(game, level)
game.draw_lines()

# Main loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
            x, y = pygame.mouse.get_pos()
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
            if row < 3 and col < 3:
                game.handle_player_move(row, col)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset()

    if game.player == 2 and not game.game_over:
        ai.make_move()

    game.draw()
    pygame.display.update()

pygame.quit()
sys.exit()
