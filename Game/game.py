import pygame
import pymunk
import random
import sqlite3
import db_functions

#Initiate pygame and show the window
pygame.init()
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

#Initialize pymunk space
space = pymunk.Space()
space.gravity = 0, 900


#Frame count handling
FPS = 80


body = pymunk.Body(1, 1111111)
body.position = 200, 400
shape = pymunk.Circle(body, 20)
shape.friction = 1.0

space.add(body, shape)         


class Pilars():
    def __init__(self, x, space, display):
        self.display = display
        
        self.length = random.randint(100, 670)
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = x, self.length/2
        self.shape = pymunk.Poly.create_box(self.body, (50, self.length))
        
        self.length_second = 800 - (self.length + 60)
        self.body_second = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body_second.position = x, self.length + 60 + self.length_second/2
        self.shape_second = pymunk.Poly.create_box(self.body_second, (50, self.length_second))
        
        space.add(self.body, self.shape)
        space.add(self.body_second, self.shape_second)
        
    def draw(self):
        rect_top = (self.body.position[0], self.body.position[1], 50, self.length)
        rect_bottom = (self.body_second.position[0], self.body_second.position[1], 50, self.length_second)
        
        pygame.draw.rect(self.display, (0, 0, 255), rect_top)
        pygame.draw.rect(self.display, (0, 0, 255), rect_bottom)
        
        print(rect_top)
        print(rect_bottom)
        
pilars = Pilars(400, space, display)
        
def game():
    sc = 0
    
    while True:
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return sc
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    body.apply_impulse_at_local_point((0, -400))
                            
                
        display.fill((255, 255, 255))
        
        pygame.draw.circle(display, (255, 0, 0), (body.position), 20)
        pilars.draw()
              
        pygame.display.flip()
        space.step(1/FPS)
        clock.tick(FPS)        
        

# Enter x into the table under the "score" column
x = game()

db_functions.insertData('Tester', x)