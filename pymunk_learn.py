import pymunk
import pygame

pygame.init()
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, -1000
FPS = 50
dt = 1.0 / FPS

def convert_coordinates(point):
    return point[0], 800-point[1]

body = pymunk.Body()
body.position = 400, 600
shape = pymunk.Circle(body, 10)
shape.density = 1
space.add(body, shape)

body2 = pymunk.Body()
body2.position = 400, 550
shape2 = pymunk.Circle(body2, 10)
shape2.density = 1
space.add(body2)

# segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
# segment_shape = pymunk.Segment(segment_body, (0, 50), (800, 50), 5)
# space.add(segment_shape)

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((255, 255, 255))
        x, y = convert_coordinates(body.position)
        pygame.draw.circle(display, (255, 0, 0), (int(x), int(y)), 10)
        pygame.draw.line(display, (0, 0, 0), (0, 750), (800, 750), 5)
        pygame.display.update()
        clock.tick(FPS)
        # print dt
        space.step(dt)

game()
pygame.quit()