"""
    Create a display surface and caption it. Download an image of a small ball and
    import that image into your program.
    Create a wall of some thickness all around the display surface, i.e., a
    perimeter along the display surface with a different color than your background.
    Make the initial position of the ball random, i.e., the ball's initial position
    should vary everytime your code is run.
    
    Write code such that the ball keeps bouncing between these four walls either
    logically or arbitrarily.
    
    Also, write a code that counts the number of bounces on each wall, displays
    this count at a corner of your surface, and keeps updating the count as the
    ball keeps bouncing. 
    
    Note: Try to play around with colors as well.
    Hint: Recall that any action can be performed by writing code for various events.
            How to code a ball that bounces off of all four walls?
"""

import pygame
import random

pygame.init()

one = (255, 0, 0)
two = (0, 255, 0)
three = (0, 0, 255)
black = (0, 0, 0)
gameSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("multiple bounce with counter")
count = 0
ball = pygame.image.load("circle-outline-2.png")
font_name = pygame.font.match_font('arial')
#function for displaying the word (learnt from internet)
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def main():
    # Write your pygame code (the "while" loop) in this "main" function.
    gameExit = False

    
    deltax = 12
    deltay = 18
    x = random.randint(0,700)
    y = random.randint(0,445)
    count = 0
    #running the program
    while not gameExit:
        for event in pygame.event.get():
            print event
            if event.type == pygame.QUIT:
                gameExit = True
                
        x += deltax
        y += deltay
        
        #bounce back
        if x < -10 or x > 660:
            deltax *= -1
            count += 1
        if y < 0 or y > 432:
            deltay *= -1
            count += 1
            
        gameSurface.fill(one)

        
        #pygame.draw.circle(gameSurface, red, (x, y), 10, 0)
        gameSurface.blit(ball,(x,y))
        
        pygame.draw.rect(gameSurface, two, (0, 550, 1000, 50))
        #display the count
        draw_text(gameSurface, str(count), 100, 100, 100)
        pygame.display.update()
        
    pygame.quit()

    quit()


if __name__ == '__main__':
    main()