import pygame
from classBall import * 

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
              
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [800, 600]
screen = pygame.display.set_mode(size)
 
#Window Caption
pygame.display.set_caption("RedDot") 
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates [FPS]
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [255,0,0]
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get(): #procedure to exit
        if event.type == pygame.QUIT:
            done = True           
 
    # --- Game Logic
 
    # Move the object according to the speed vector.
    theBall.move()
    
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
 
   
    theBall.draw(screen)
    
 
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second [SetFPS]
    clock.tick(60)
    
# Close the window and quit.
pygame.quit()
