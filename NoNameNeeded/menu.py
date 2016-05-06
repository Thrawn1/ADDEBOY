import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
# Setup
pygame.init()
pygame.image.load("csh.jpg")
pygame.image.load("11.jpg")


# Set the width and height of the screen [width,height]
size = [800, 600]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("menu")
background_image = pygame.image.load("csh.jpg")
background_image=pygame.image.load("csh.jpg").convert()
player_image = pygame.image.load("11.jpg").convert()
player_image.set_colorkey(BLACK)
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(1)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        
    # --- Game Logic
        player_position = pygame.mouse.get_pos()
        x=player_position[0]
        y=player_position[1]
        screen.blit(player_image, [x,y])
 
 
    # Go ahead and update the screen with what we've drawn.
    
    screen.blit(background_image, [0,0])
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
