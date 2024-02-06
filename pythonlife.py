import pygame
import sys
from build import Carnivore, createHerd


pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Habitat")

# Set up the clock
clock = pygame.time.Clock()

# Set the desired FPS
fps = 30
# create some boys
bodies = []
travelPath = []
predators = createHerd(Carnivore,10,'Red',bodies, windowWidth=width, windowHeight=height,travelPath=travelPath)

def draw(surface, x, y, color, size: float):
    for i in range(0, size):
        pygame.draw.line(surface, color, (x, y - 1), (x, y + 2), abs(size))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game logic and drawing code here
    screen.fill(0)

    for i in range(len(bodies)):
        draw(screen, bodies[i].x, bodies[i].y, bodies[i].colour, size=3)



    pygame.display.flip()

    # Control the frame rate
    clock.tick(fps)
