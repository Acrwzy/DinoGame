
# Libraries used 
import sys
import pygame

# Dimensions of the window
WIDTH = 623
HEIGHT = 150

# Initializing PyGame Library
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dino')

def main():
    # Main loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
        pygame.display.update

main()