import pygame

#Функциялар
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

# Тегіс сызықтар салу функциясы
def roundline(canvas, color, start, end, radius=1):
    x_axis = end[0] - start[0]
    y_axis = end[1] - start[1]
    dist = max(abs(x_axis), abs(y_axis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * x_axis)
        y = int(start[1] + float(i) / dist * y_axis)
        pygame.draw.circle(canvas, color, (x, y), radius)

# Паигеимды инициализациялайды -
pygame.init()

# дисплейды орнату
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Paint pygame")

# түстерді анықтау
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
light_blue = (0, 255, 255)
pink = (255, 0, 255)

# Бастапқы мәндерді орнату
color = blue
last_pos = (0, 0)
mouse_down = False
screen.fill(white)
pygame.display.update()
radius = 5

#ФПС
clock = pygame.time.Clock()
running = True

# Негізгі ойын циклі
while running:
    for event in pygame.event.get():
        # Ойыннан шығу
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Пернетақтаны (клавиатура) енгізу арқылы түсін өзгерту
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
            
            # Пернетақтаны енгізу арқылы өшіру
            if event.key == pygame.K_e:
                erase()
            
            # өшіргіш құралына өзгерту
            if event.key == pygame.K_w:
                color = white
                radius = 20
            
            # Тіктөртбұрыш сызу
            if event.key == pygame.K_p:
                rectangle()
            
            # Шеңбер сызу (Домалақ)
            if event.key == pygame.K_c:
                circle()
            
        # Тышқанмен (щеткамен)енгізу
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
