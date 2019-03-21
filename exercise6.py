import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1000, 400), 0, 24)

image1_filename = 'IMG_6245.jpg'
image2_filename = 'IMG_6459.jpg'
image3_filename = 'IMG_6819.jpg'


bgimage1 = pygame.image.load(image1_filename).convert()
bgimage2 = pygame.image.load(image2_filename).convert()
bgimage3 = pygame.image.load(image3_filename).convert()

bgimage = [bgimage1, bgimage2, bgimage3]


x1, y1 = 0, 0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()


    x1 -= 2 
    if x1 <= -400:
        bgimage = bgimage[1:]+bgimage[:1]
       
        bgimage1, bgimage2, bgimage3 = bgimage
        x1 = 0
   

    screen.blit(bgimage1, (x1, y1))
    screen.blit(bgimage2, (x1+400, y1))
    screen.blit(bgimage3, (x1+800, y1))
    

    pygame.display.update()
