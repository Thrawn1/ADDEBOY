import pygame
from classCube import *
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
 
cube = Cube()
cube.rect_x = 100
cube.rect_y = 100
cube.change_x = 5
cube.change_y = 5
cube.rect_color = [255,255,255]

cube2 = Cube()
cube2.rect_x = 300
cube2.rect_y = 300
cube2.change_x = -5
cube2.change_y = -5
cube2.rect_color = [255,0,0]

# -------- Main Program Loop  -----------
while done==False: #Procedure procedure to exit
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True 
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(black)
 
    # Draw Cube
    cube.draw(screen)
    cube2.draw(screen)
    
    # Cube Change StartPosition
    cube.move()
    cube2.move()
    
    # Cube Ricochet
    if cube.rect_y > 550 or cube.rect_y < 0:
        cube.change_y = cube.change_y * -1
    if cube.rect_x > 750 or cube.rect_x < 0:
        cube.change_x = cube.change_x * -1
    if cube2.rect_y > 550 or cube2.rect_y < 0:
        cube2.change_y = cube2.change_y * -1
    if cube2.rect_x > 750 or cube2.rect_x < 0:
        cube2.change_x = cube2.change_x * -1
   
    #def Cross(self):
        #if self.rect_y == other
             
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 

pygame.quit()
