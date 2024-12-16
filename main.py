import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #init pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #game loop
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        screen.fill((0,0,0))
        pygame.display.flip()



if __name__ == "__main__":
    main()


