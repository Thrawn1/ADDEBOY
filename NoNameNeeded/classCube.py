import pygame
class Cube():
    # --- Атрибуты класса ---
    # Ball position
    rect_x=50
    rect_y=50
 
    # Cube vector
    change_x=5
    change_y=5
 
   
    # Cube color
    rect_color=[255,255,255]
 
    # --- Методы класса ---
    def move(self):
        self.rect_x += self.change_x
        self.rect_y += self.change_y
             
    def draw(self, screen):
        pygame.draw.rect(screen,self.rect_color,[self.rect_x,self.rect_y,50,50])
      