import pygame
import pymunk.pygame_util
import pymunk
import sqlite3

#Initiate pygame and show the window
pygame.init()
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(display)

#Initialize pymunk space
space = pymunk.Space()
space.gravity = 0, 900


#Frame count handling
FPS = 80


body = pymunk.Body(1, 1111111)
body.postition = 700, 400
shape = pymunk.Circle(body, 20)
shape.friction = 1
       
space.add(body, shape)        
        

    
    
        
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
        space.debug_draw(draw_options)       
        pygame.display.flip()
        space.step(1/FPS)
        clock.tick(FPS)

        sc += 1
        
        

# Enter x into the table under the "score" column
x = game()