import pymunk
import pymunk.pygame_util
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = 0, 900  # gravity going down



# Create a jumping body
body = pymunk.Body(1, 1111111)
body.position = 400, 300
shape = pymunk.Circle(body, 20)
shape.friction = 1.0
space.add(body, shape)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                    body.apply_impulse_at_local_point((0, -400))
                    print("space")

    screen.fill((255, 255, 255))
    space.debug_draw(draw_options)
    pygame.display.flip()
    space.step(1 / 60.0)
    clock.tick(60)