#Ultpygame project by Ceon v idk
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('img/ultpy/Sky.png')
ground_surface = pygame.image.load('img/ultpy/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(ground_surface(0,0))
    screen.blit(sky_surface,(200,100))

    


    pygame.display.update()
    clock.tick(60)