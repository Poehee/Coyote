import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

clock = pygame.time.Clock()

FPS = 60 # How many times the screen will update per second

screen_width = 1280 # How wide the window will be
screen_height = 1024 # how high the window will be

screen = pygame.display.set_mode([screen_width, screen_height]) # creates the screen
surface_pos = [590,462]

# Variable to keep the main loop running
running = True
while running:
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill([255, 255, 255])
    sf = pygame.Surface([100,100])
    sf.fill([50,50,50])
    rect = sf.get_rect()

    screen.blit(sf, surface_pos)
    surface_pos[0] += 1
    surface_pos[1] += 1
    
    pygame.display.flip()

pygame.quit()