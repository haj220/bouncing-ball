"""
    Create a display surface and caption it. Create a ball on this surface.
    
    Write code such that the ball keeps moving left as long as the left arrow key is
    pressed and stops immediately as soon as the key is released, keeps moving up
    as long as the up arrow key is pressed and stops immediately as soon as the key
    is released, and so on.
    
    Note: Try to play around with colors as well.
    Hint: Recall that any action can be performed by writing code for various events.
            Refer to the KEYUP event.
"""

import pygame


pygame.init()

   
   
   
surface_height = 400
surface_weight = 400
x=surface_weight/4
y=surface_height/4
FPS = 30
#create the surface
gameSurface = pygame.display.set_mode((400, 400))
pygame.display.update()


pygame.display.set_caption("title")
#game control variable 
gameExit = False
#create color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
clock = pygame.time.Clock()
#running game
while not gameExit:
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT:
            gameExit = True
    #setup direction 
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
                x-=10
        if event.key == pygame.K_RIGHT:
                x+=10
        if event.key == pygame.K_UP:
                y-=10
        if event.key == pygame.K_DOWN:
                y+=10
        
        
    gameSurface.fill(white)
    pygame.draw.circle(gameSurface, green, (x,y),5,5)
    gameSurface.fill(red,(100,200,20,40))
    clock.tick(FPS)
    pygame.display.update()
    
pygame.quit()
quit()


