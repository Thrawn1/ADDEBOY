import pygame
class Ball():
    # --- Атрибуты класса ---
    # Ball position
    x=0
    y=0
 
    # Ball's vector
    change_x=0
    change_y=0
 
    # Ball size
    size=10
 
    # Ball color
    color=[255,255,255]
 
    # --- Методы класса ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
             
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size )