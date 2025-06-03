import pygame
import pymunk
import random
import db_functions
import math

extra_lives = True

#Initiate pygame and show the window
pygame.init()
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

#Initialize pymunk space
space = pymunk.Space()
space.gravity = 0, 900


#Frame count handling
FPS = 80


#Ball pymunk
body = pymunk.Body(1, 1111111)
body.position = 200, 400
shape = pymunk.Circle(body, 20)
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
        self.rect_top = (self.body.position[0] - 25, 0, 70, self.length)
        self.rect_bottom = (self.body_second.position[0] - 25, self.length + 100, 70, self.length_second)
        
        pygame.draw.rect(self.display, (0, 0, 255), self.rect_top)
        pygame.draw.rect(self.display, (0, 0, 255), self.rect_bottom)
        
        #Redo the cycle
        if self.body.position[0] < -70:
            self.set_new_position(900)
            
    def has_collided(self, pos, radius):
        #Has collided with the ball
        return (self.body.position[0] - 35) == (pos[0] + radius) and (pos[1] <= self.length or pos[1] >= self.length + 100)
    
    
class Coin():
    def __init__(self, x, space, display):
        self.isDeleted = False
        self.x = x
        self.display = display
        self.body = pymunk.Body(0, 0, body_type=pymunk.Body.KINEMATIC)
        self.body.position = self.x, random.randint(15, 785)
        self.body.velocity = -100, 0
        self.shape = pymunk.Circle(self.body, 20)
        self.shape.sensor = True
    
        space.add(self.body, self.shape)
        
    def set_new_position(self, x):
        self.isDeleted = False
        self.x = x
        self.shape.density = 0
        self.body = pymunk.Body(0, 0, body_type=pymunk.Body.KINEMATIC)
        self.body.position = self.x, random.randint(15, 785)
        self.body.position = -100, 0
        self.shape = pymunk.Circle(self.body, 20)
        self.shape.elasticity = 0
        self.display = display
        self.shape.sensor = True
        
        space.add(self.body, self.shape)
        
    def has_collided(self, pos, radius):
        #Has collided with the ball
        
        x_distance = pos[0] - self.body.position[0]
        y_distance = pos[1] - self.body.position[1]
        
        center_distance = math.sqrt(x_distance ** 2 + y_distance ** 2)
        
        if center_distance < radius + 20:
            self.isDeleted = True
            return True
        
        else:
            return False

    
    def draw(self):
        if self.isDeleted == False:
            pygame.draw.circle(self.display, (255, 255, 0), self.body.position, 10)
        
        #Redo Cycle        
        if self.body.position[0] < -20:
            self.set_new_position(900)
    
            

#Make three pilars     
pilars = Pilars(400, space, display)
pilars_two = Pilars(700, space, display)
pilars_three = Pilars(1000, space, display)

#Three coins to go in between the pilars
coin = Coin(650, space, display)
coin_two = Coin(850, space, display)
coin_three = Coin(1150, space, display)


#Make the game function return the score        
def game():
    sc = 0    
    
    #Game loop
    while True:
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Will break when the score's returned
                return sc
            
            #Jump on space
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    body.apply_impulse_at_local_point((0, -400))
                    

        
        #Background       
        display.fill((255, 255, 255))
        
        #Draw the ball
        pygame.draw.circle(display, (255, 0, 0), (body.position), 20)
        
        #Draw the pilars
        pilars.draw()
        pilars_two.draw()
        pilars_three.draw()
        
        #Draw the coins
        coin.draw()
        coin_two.draw()
        coin_three.draw()
        
        #End the game if any of the pilars collide with the ball
        if pilars.has_collided(body.position, 20):
            return sc
        
        if pilars_two.has_collided(body.position, 20):
            return sc
        
        if pilars_three.has_collided(body.position, 20):
            return sc
        
        
        # Add a point to the score and make the coin disappear upon colliding with the ball
        if coin.has_collided(body.position, 20) and coin.isDeleted and coin.isDeleted == False:
            sc += 1
            coin.set_new_position(coin.body.position[0] + 800)
        
        if coin_two.has_collided(body.position, 20) and coin_two.isDeleted == False:
            sc += 1
            coin_two.set_new_position(coin_two.body.position[0] + 800)
            
        if coin_three.has_collided(body.position, 20) and coin_three.isDeleted == False:
            sc += 1
            coin_three.set_new_position(coin_three.body.position[0] + 800)
            
        
        if body.position[1] > 780 or body.position[1] < 20:
            return sc
        
              
        pygame.display.flip()
        space.step(1/FPS)
        clock.tick(FPS)
        

# Enter x into the table under the "score" column
x = game()

#db_functions.insertData('Tester', x)