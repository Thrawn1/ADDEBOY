import pygame
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

def draw_stick_figure(screen,x,y):
    # Head
    #circle(Surface, color, pos, radius, width=0)
    #pygame.draw.ellipse(screen,black,[96+x,83+y,10,10],0)
    pygame.draw.circle(screen, black, [101+x,88+y],4)
 
    # Legs
    pygame.draw.line(screen,black,[100+x,100+y],[105+x,110+y],2)
    pygame.draw.line(screen,black,[100+x,100+y],[95+x,110+y],2)
 
    # Body
    pygame.draw.line(screen,black,[100+x,100+y],[100+x,90+y],2)
 
    # Hands
    pygame.draw.line(screen,black,[100+x,90+y],[104+x,100+y],2)
    pygame.draw.line(screen,black,[100+x,90+y],[96+x,100+y],2)
    
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("DrawStick")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# --------  Main Program Loop -----------
while done==False:  #Procedure procedure to exit
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True 
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(white)
 
 
    # --- Drawing code should go here
    draw_stick_figure(screen, 50, 50) 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 

pygame.quit()
