import pygame
import math

# Функция
def erase():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 30
    rect_height = 30
    pygame.draw.rect(screen, white, (rect_pos, (rect_width, rect_height)))

def circle():
    circle_pos = pygame.mouse.get_pos()
    circle_radius = 30
    pygame.draw.circle(screen, color, circle_pos, circle_radius)

def rectangle():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 50
    rect_height = 50
    pygame.draw.rect(screen, color, (rect_pos, (rect_width, rect_height)))

def square():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 50
    rect_height = 50
    pygame.draw.rect(screen, color, (rect_pos, (rect_width, rect_height)))

def right_triangle():
    start_pos = pygame.mouse.get_pos()
    rect_width = 50
    rect_height = 50
    pygame.draw.polygon(screen, color, [(start_pos[0], start_pos[1]), (start_pos[0], start_pos[1] + rect_height), (start_pos[0] + rect_width, start_pos[1])])

def equilateral_triangle():
    start_pos = pygame.mouse.get_pos()
    side = 50
    height = math.sqrt(side**2 - (side/2)**2)
    pygame.draw.polygon(screen, color, [(start_pos[0], start_pos[1]), (start_pos[0] + side, start_pos[1]), (start_pos[0] + side/2, start_pos[1] - height)])

def rhombus():
    pos = pygame.mouse.get_pos()
    side_length = 50
    top = (pos[0], pos[1] - side_length)
    bottom = (pos[0], pos[1] + side_length)
    left = (pos[0] - side_length, pos[1])
    right = (pos[0] + side_length, pos[1])
    
    # Рисовать ромб
    pygame.draw.polygon(screen, color, [top, right, bottom, left])


# Функция для рисования плавных линий
def roundline(canvas, color, start, end, radius=1):
    x_axis = end[0] - start[0]
    y_axis = end[1] - start[1]
    dist = max(abs(x_axis), abs(y_axis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * x_axis)
        y = int(start[1] + float(i) / dist * y_axis)
        pygame.draw.circle(canvas, color, (x, y), radius)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Paint pygame")

# определить цвета
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
light_blue = (0, 255, 255)
pink = (255, 0, 255)

# Установить начальные значения
color = blue
last_pos = (0, 0)
mouse_down = False
screen.fill(white)
pygame.display.update()
radius = 5

#FPS
clock = pygame.time.Clock()
running = True

# основной цикл игры
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = red
                radius = 5
            elif event.key == pygame.K_b:
                color = blue
                radius = 5
            elif event.key == pygame.K_g:
                color = green
                radius = 5
            elif event.key == pygame.K_y:
                color = yellow
                radius = 5
            elif event.key == pygame.K_q:
                color = black 
                radius = 5
            
            # Erase with keyboard input
            if event.key == pygame.K_e:
                erase()
            
            # Change to eraser tool
            if event.key == pygame.K_w:
                color = white
                radius = 20
            
            # Draw a rectangle
            if event.key == pygame.K_p:
                rectangle()
            
            # Draw a circle
            if event.key == pygame.K_c:
                circle()
            #Draw a square
            if event.key == pygame.K_s:
                square()
            #Draw a right triangle
            if event.key == pygame.K_t:
                right_triangle()
            #Draw a equilateral triangle
            if event.key == pygame.K_l:
                equilateral_triangle()
            if event.key == pygame.K_h:
                rhombus()
        # Мышь (кисть) ввод
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, color, event.pos, 5)
            mouse_down = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        
        if event.type == pygame.MOUSEMOTION:
            if mouse_down:
                pygame.draw.circle(screen,color,event.pos,radius)
                roundline(screen,color,event.pos,last_pos,radius)
            last_pos = event.pos

        pygame.display.update()
        clock.tick(60)

