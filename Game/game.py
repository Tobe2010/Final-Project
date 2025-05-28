import pygame
import pymunk
import sqlite3

#Initiate pygame and show the window
pygame.init()
display = pygame.display.set_mode((800, 800))

#Initialize pymunk space
space = pymunk.Space()
space.gravity = 0, 100

# Convert pymunk position to pygame position
def convert_pos(coordinates):
    return int(coordinates[0]), int(coordinates[1])

#Frame count handling
clock = pygame.time.Clock()
FPS = 80


class Ball():
    def __init__(self, color, space):
        self.color = color
        self.body = pymunk.Body(1, 1666)
        self.body.postition = 400, 400
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.elasticity = 1
       
        space.add(self.body, self.shape)
        

    def draw(self, display, x, shouldJump):        
        pygame.draw.circle(display, self.color, (x, self.body.position[1]), 15)
        
        if shouldJump:
            self.body.apply_impulse_at_local_point(pymunk.Vec2d(0, -1))
        

#class Rectangle():
    #def __init__(self, )
    
    
ball = Ball((255, 0, 0), space)
        
def game():
    sc = 0
    jump = False
    
    while True:
        space.step(0.02)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
            if event.type == pygame.KEYDOWN:
                jump = event.key == pygame.K_SPACE
        
        display.fill((255, 255, 255))
        
        ball.draw(display, 400, jump)
                
        pygame.display.update()
        clock.tick(FPS)
        
        sc += 1
        
        

# Enter x into the table under the "score" column
x = game()