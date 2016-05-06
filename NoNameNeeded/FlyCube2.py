import pygame
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("FlyCube")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Set first position cube
rect_x = 50
rect_y = 50
# Vector cube
rect_change_x = 5
rect_change_y = 5
# Set first position cube
rect1_x = 500
rect1_y = 500
# Vector cube
rect1_change_x = -5
rect1_change_y = -5

rect_color = white
rect1_color = red

# -------- Main Program Loop  -----------
while done==False: #Procedure procedure to exit
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True 
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(black)
 
    # Draw Cube
    a = pygame.draw.rect(screen,rect_color,[rect_x,rect_y,50,50])
    b = pygame.draw.rect(screen,rect1_color,[rect1_x,rect1_y,50,50])
 
    # Cube Change StartPosition
    rect_x += rect_change_x
    rect_y += rect_change_y
     
    rect1_x += rect1_change_x
    rect1_y += rect1_change_y
    # Cube Ricochet
    if rect_y > 550 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 750 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if rect1_y > 550 or rect1_y < 0:
        rect1_change_y = rect1_change_y * -1
    if rect1_x > 750 or rect1_x < 0:
        rect1_change_x = rect1_change_x * -1
    if a == b:
        rect_change_y = rect_change_y * -1
        rect1_change_y = rect1_change_y * -1
        rect_change_x = rect_change_x * -1
        rect1_change_x = rect1_change_x * -1 
         
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 

pygame.quit()
