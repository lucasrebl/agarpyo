import pygame
from game import Game

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Agarpyo by lucas')
    
if __name__ == "__main__":
    game = Game(width, height, screen)
    game.run()
