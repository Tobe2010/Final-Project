import pygame
import pymunk
import sqlite3

#Initiate pygame and show the window
pygame.init()
display = pygame.display.set_mode((800, 800))

#Initialize pymunk space
space = pymunk.Space()
space.gravity = 0, -10

# Convert pymunk position to pygame position
def convert_pos(coordinates):
    return int(coordinates[0]), 800 - int(coordinates[1])

#Frame count handling
clock = pygame.time.Clock()
FPS = 80


class Ball():
    def __init__(self, x, color):
        self.color = color
        self.body = pymunk.Body(1, 1666)
        self.body.postition = x, 400
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.elasticity = 1
       
        space.add(self.body, self.shape)
        
    def printPos(self):
        print(self.body.position)
        
    def pos(self):
        return self.body.position
    
    def draw(self):        
        pygame.draw.circle(display, self.color, self.body.postition, 15)
        

#class Rectangle():
    #def __init__(self, )
    
    
ball = Ball(400, (255, 0, 0))
        
def game():
    sc = 0
    
    while True:
        space.step(0.02)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return sc
            
        display.fill((255, 255, 255))
                    

        pygame.draw.circle(display, (255,0, 0), convert_pos(ball.pos()), 15)
        
        pygame.display.update()
        clock.tick(FPS)
        
        sc += 1
        
        ball.printPos()
        

# Enter x into the table under the "score" column
x = game()