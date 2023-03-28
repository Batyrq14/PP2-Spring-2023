import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")
# icon = pygame.image.load(r'C:\Users\Batyrkhan\OneDrive\Рабочий стол\PYTHON GITHUB\TSIS_7\ball movement\Fasticon-Angry-Birds-Red-bird.32.png')
# pygame.display.set_icon(icon)
# Set up the ball
ball_radius = 25
ball_pos_x = screen_width // 2
ball_pos_y = screen_height // 2
ball_color = (255, 0, 0)  # Red
ballX_change = 0
ballY_change = 0

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left 
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX_change = -0.3
            if event.key == pygame.K_RIGHT:
                ballX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ballX_change = 0
        
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ballY_change = -0.3
            if event.key == pygame.K_DOWN:
                ballY_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ballY_change = 0
    
    ball_pos_x += ballX_change
    ball_pos_y += ballY_change
    
    if ball_pos_x <= 25:
        ball_pos_x = 25
    elif ball_pos_x >= 775:
        ball_pos_x = 775
    if ball_pos_y >= 572:
        ball_pos_y = 572
    elif ball_pos_y <= 25:
        ball_pos_y = 25

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_pos_x, ball_pos_y), ball_radius)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()