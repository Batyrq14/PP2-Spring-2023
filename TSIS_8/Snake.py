import pygame
from random import randrange

WINDOW = 700
TILE_SIZE = 25
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]

snake = pygame.rect.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
snake.center = get_random_position()

length = 1
segments = [snake]
snake_dir = [0, 0]

time, time_step = 0, 110
pygame.init()
food = pygame.rect.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
food.center = get_random_position()
pygame.font.init()
score = 0
level = 1
font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()

#инициализируем счет и уровень 0
score = 0
level = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_dir = (0 , -TILE_SIZE)
            if event.key == pygame.K_s:
                snake_dir = (0, TILE_SIZE)
            if event.key == pygame.K_a:
                snake_dir = (-TILE_SIZE,0)
            if event.key == pygame.K_d:
                snake_dir = (TILE_SIZE,0)
                
                
    screen.fill('black')
    #проверяем границы 
    
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW:
        snake.center, food.center = get_random_position() , get_random_position()
        length , snake_dir = 1, (0,0)
        segments = [pygame.rect.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)]
        segments[0].center = snake.center
        score = 0  # сбросить счет на 0
        level = 0  # сбросить уровень на 0
        
    #check food 
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
        score += 10 # увеличиваем счет на 10 за каждую съеденную еду
        
        # увеличиваем уровень, если счет кратен 30
        if score % 30 == 0:
            level += 1
            
            # уменьшаем time_step, чтобы увеличить скорость для каждого уровня
            time_step -= 5
        
    # создаем текстовые поверхности для счета и уровня
    score_surface = font.render(f"Score: {score}", True, 'white')
    level_surface = font.render(f"Level: {level}", True, 'white')
    
    # выводим счет и уровень на экран
    screen.blit(score_surface, (10, 10))
    screen.blit(level_surface, (10, 50))
    
    #рисуем еду 
    pygame.draw.rect(screen,'red', food)
    #рисуем змею 
    for segment in segments:
        pygame.draw.rect(screen, 'green', segment)
    #движение змеи
    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(pygame.rect.Rect(snake.x, snake.y, TILE_SIZE - 2, TILE_SIZE - 2))
        segments = segments[-length:]
    pygame.display.update()
   

