import pygame
import time
import random

# تهيئة اللعبة
pygame.init()

# إعدادات الشاشة
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# ألوان
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# إعدادات الثعبان
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

def show_message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            show_message("Game Over! Press C-Play Again or Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # تحقق من خروج الثعبان خارج الشاشة
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > length:
            del snake[0]

        # تحقق من الاصطدام بنفسه
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake)
        pygame.display.update()

        # تحقق من أكل الطعام
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
