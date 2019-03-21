import pygame
import random

white = [0,0,0]

def main():
    clock = pygame.time.Clock()
    # Write your pygame code (the "while" loop) in this "main" function.
    screen_height=500
    screen_width=500
    gameSurface = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('5')
    pygame.display.update()
    
    #x,y coordinates, radius, speed and color of the ball
    x=[] 
    y=[] 
    r=[] 
    deltax=[] 
    deltay=[] 
    color=[] 
    
                    

    #create number for each of ten balls           
    for i in range (10): 
        x.append(random.randrange(100,500))
        y.append(random.randrange(100,500))
        r.append(random.randrange(20, 50))
        deltax.append(random.randrange(-5,5))
        deltay.append(random.randrange(-5,5))
        color.append(random.randrange(0, 255))
        
        
        
        
    gameExit =False
    #loop for running
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
        gameSurface.fill(white)

        
        for i in range (10):
            pygame.draw.circle(gameSurface,(color[i],0,0),(x[i],y[i]),r[i])
        
        
        for i in range (10):
            #move the ball
            x[i] += deltax[i]
            y[i] += deltay[i]
            
            #shrink the size
            r[i] -= 3
 

            
            #change the color to black
            if color[i]-5 >=0:
                color[i] -= 5
            
 
 
            #if radius smaller than 20 disappear
            if r[i] < 20:
                r[i] = random.randrange(20, 50)
                x[i] = random.randint(100,500)
                y[i] = random.randint(100,500)
                color[i] =255
                

            
                
                
                
            #bounce back
            if y[i] > screen_height - r[i] or y[i] < r[i]:
                deltax[i] *= -1
    
            if x[i] > screen_width - r[i] or x[i] < r[i]:
                deltay[i] *= -1
                
        clock.tick(10)    
        pygame.display.update()


if __name__ == '__main__':
    main()
    

pygame.quit()
