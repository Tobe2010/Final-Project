import pygame
import pymunk
import random
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
shape.collision_type = 1

space.add(body, shape)
         


class Pilars():
    def __init__(self, x, space, display):
        self.x = x
        self.display = display
        
        self.length = random.randint(100, 670)
        self.body = pymunk.Body(0, 0, body_type=pymunk.Body.KINEMATIC)
        self.body.position = self.x, self.length/2
        self.shape = pymunk.Poly.create_box(self.body, (70, self.length))
        self.shape.collision_type = 2
        self.body.velocity = -100, 0
        
        self.length_second = 800 - (self.length + 100)
        self.body_second = pymunk.Body(0, 0, body_type=pymunk.Body.KINEMATIC)
        self.body_second.position = self.x, self.length + 100 + self.length_second/2
        self.shape_second = pymunk.Poly.create_box(self.body_second, (70, self.length_second))
        self.shape_second.collision_type = 2
        self.body_second.velocity = -100, 0
        
        
        space.add(self.body, self.shape)
        space.add(self.body_second, self.shape_second)
        
    def set_new_position(self, x):
        self.x = x
        
        self.length = random.randint(100, 670)
        self.body = pymunk.Body(0, 0, body_type=pymunk.Body.KINEMATIC)
        self.body.position = self.x, self.length/2
        self.shape = pymunk.Poly.create_box(self.body, (70, self.length))
        self.shape.collision_type = 2
        self.body.velocity = -100, 0
        
        self.length_second = 800 - (self.length + 100)
        self.body_second = pymunk.Body(0, 0, body_type=pymunk.Body.KINEMATIC)
        self.body_second.position = self.x, self.length + 100 + self.length_second/2
        self.shape_second = pymunk.Poly.create_box(self.body_second, (70, self.length_second))
        self.shape_second.collision_type = 2
        self.body_second.velocity = -100, 0
        
        space.add(self.body, self.shape)
        space.add(self.body_second, self.shape_second)
        
    def draw(self):
        rect_top = (self.body.position[0] - 25, 0, 70, self.length)
        rect_bottom = (self.body_second.position[0] - 25, self.length + 100, 70, self.length_second)
        
        pygame.draw.rect(self.display, (0, 0, 255), rect_top)
        pygame.draw.rect(self.display, (0, 0, 255), rect_bottom)
        
        #Redo the cycle
        if self.body.position[0] < -70:
            self.set_new_position(900)
            
            
def on_collide(arbiter, space, data):
    return True

        
pilars = Pilars(400, space, display)
pilars_two = Pilars(700, space, display)
pilars_three = Pilars(1000, space, display)
        
def game():
    sc = 0
    counter = 0
    
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
        pilars_two.draw()
        pilars_three.draw()
        
        counter += 1
        if counter % 50 == 0:
            sc += 1
        
        #print(shape.shapes_collide(pilars.shape).points)
        
        #if len(shape.shapes_collide(pilars.shape).points) > 0:
        #    return sc
        
        #if len(shape.shapes_collide(pilars_two.shape).points) > 0:
         #   return sc
        
        #if len(shape.shapes_collide(pilars_three.shape).points) > 0:
        #    return sc
        
        #if len(shape.shapes_collide(pilars_four.shape).points) > 0:
        #    return sc                    
        
        if body.position[1] > 780 or body.position[1] < 20 and db.queryLivesForUser(name) <= 0:
            return sc
        
              
        pygame.display.flip()
        space.step(1/FPS)
        clock.tick(FPS)
        

# Enter x into the table under the "score" column
x = game()

#db_functions.insertData('Tester', x)