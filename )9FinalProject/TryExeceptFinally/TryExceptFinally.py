#Try -- except -- else -- finally

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game Variables
player_x = 50
player_y = SCREEN_HEIGHT // 2
player_speed = 5
player_width = 20
player_height = 20

level = 1
progress = 0
max_progress = 100

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Game Template")

# Main Menu
def main_menu():
    title_font = pygame.font.SysFont(None, 60)
    difficulty_font = pygame.font.SysFont(None, 30)

    running = True
    while running:
        screen.fill(WHITE)

        title_text = title_font.render("Game Title", True, BLACK)
        screen.blit(title_text, (SCREEN_WIDTH//2 • title_text.get_width()//2, 100))

        easy_text = difficulty_font.render("Press E for Easy", True, BLACK)
        screen.blit(easy_text, (SCREEN_WIDTH//2 • easy_text.get_width()//2, 250))

        hard_text = difficulty_font.render("Press H for Hard", True, BLACK)
        screen.blit(hard_text, (SCREEN_WIDTH//2 • hard_text.get_width()//2, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    start_game("easy")
                elif event.key == pygame.K_h:
                    start_game("hard")

# Game Loop
def start_game(difficulty):
    global player_x, player_y, level, progress

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            # Add action here (e.g., jump)

        # Update progress
        progress += 1
        if progress >= max_progress:
            level += 1
            progress = 0

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
        draw_progress_bar()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

def draw_progress_bar():
    progress_bar_width = int((progress / max_progress) * SCREEN_WIDTH)
    pygame.draw.rect(screen, RED, (0, 0, progress