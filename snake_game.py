import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏窗口大小
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 设置窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('贪吃蛇游戏')
clock = pygame.time.Clock()

# 字体
font = pygame.font.SysFont('arial', 25)

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, BLOCK_SIZE, BLOCK_SIZE])

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])

def show_score(score):
    value = font.render(f"得分: {score}", True, BLACK)
    screen.blit(value, [0, 0])

def game_loop():
    game_over = False
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0
    snake_list = []
    snake_length = 1
    food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = BLOCK_SIZE

        if dx == 0 and dy == 0:
            continue  # 等待玩家开始移动

        x += dx
        y += dy

        # 撞墙检测
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True
            break

        # 身体碰撞检测
        head = [x, y]
        if head in snake_list:
            game_over = True
            break
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # 吃到食物
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)
            snake_length += 1
            score += 1

        screen.fill(WHITE)
        draw_snake(snake_list)
        draw_food((food_x, food_y))
        show_score(score)
        pygame.display.update()
        clock.tick(10)

    # 游戏结束界面
    screen.fill(WHITE)
    msg = font.render('游戏结束! 按任意键退出', True, RED)
    screen.blit(msg, [WIDTH // 6, HEIGHT // 2])
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

game_loop()
