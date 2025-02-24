import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crypto Collector")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)

# Player properties
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Coin properties
coin_size = 30
coin_speed = 5
coin_spawn_rate = 25  # Higher value means fewer coins

# Obstacle properties
obstacle_width = 70
obstacle_height = 20
obstacle_speed = 7
obstacle_spawn_rate = 40  # Higher value means fewer obstacles

# Initialize variables
score = 0
coins = []
obstacles = []
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, [x, y, player_size, player_size])

def draw_coin(coin):
    pygame.draw.ellipse(screen, GOLD, coin)

def draw_obstacle(obstacle):
    pygame.draw.rect(screen, RED, obstacle)

def move_objects(objects, speed):
    for obj in objects:
        obj.move_ip(0, speed)

def remove_off_screen_objects(objects):
    return [obj for obj in objects if obj.top < HEIGHT]

def check_collisions(player_rect, coins, obstacles):
    global score
    for coin in coins[:]:
        if player_rect.colliderect(coin):
            score += 1
            coins.remove(coin)
    for obstacle in obstacles[:]:
        if player_rect.colliderect(obstacle):
            return True
    return False

# Game loop
running = True
game_over = False
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
   
