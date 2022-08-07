# Programmer: Dani Massa

## lab3.py
## Author: Matthew Anderson
## Edits: John Rieffel
## Version: Windter 2020

'''
This program displays two bouncing balls. When each of the balls bounce, they change color.

Ball 1:
    - changes from light green to brown
    - increases the score after each bounce

Ball 2:
    - changes from light yellow to red
    - changes the color of the background (from blue to purple) after each bounce
    

Additionally, this program displays two pink balls, which wrap around the screen and change
size when they wrap. These two pink balls never exceed the size of the bouncing balls.

All balls are set to have a random velocity.
'''

import pygame
import random
import math


def run_game():
    
    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    ## Open the pygame window with the specified width and height. We
    ## call our pygame window 'my_win'.    
    width = 640
    height = 480
    my_win = pygame.display.set_mode((width,height))

    ## ---------------------------------------------------------------------
    ##   Initialize Game State
    ## ---------------------------------------------------------------------
    
    ## Set up game objects.  Note that a block is just a circle, and 
    ## that a ball is a circle with a velocity.  The parentheses
    ## (tuples) separate the components in a meaningful way.  A circle
    ## is a point and a radius.  A ball is a circle (which is a point
    ## and a radius) and velocity (which has an x and y component).

    score = 0
    #ball1
    ballr = 40
    ballx = random.randint(0+ballr,width-ballr)
    bally = random.randint(0+ballr,height-ballr)
    xvel = random.randint(-3,3)
    xvel != 0
    yvel = random.randint(-3,3)
    yvel != 0
    ballcolor = pygame.color.Color('#99FF99')

    
    #ball2
    ballr2 = 40
    balla = random.randint(0+ballr2,width-ballr2)
    ballb = random.randint(0+ballr,height-ballr)
    xvel2 = random.randint(-3,3)
    xvel2 != 0
    yvel2 = random.randint(-3,3)
    yvel2 != 0
    ballcolor2 = pygame.color.Color('firebrick')

    #ball3
    ballr3 = 20
    ballm = random.randint(0+ballr3,width-ballr3)
    balln = random.randint(0+ballr3,height-ballr3)
    xvel3 = random.randint(-3,3)
    xvel3 != 0
    yvel3 = random.randint(-3,3)
    yvel3 != 0
    ballcolor3 = pygame.color.Color('hot pink')

    #ball4
    ballr4 = 20
    ballp = random.randint(0+ballr4,width-ballr4)
    ballq = random.randint(0+ballr4,height-ballr4)
    xvel4 = random.randint(-3,3)
    xvel4 != 0
    yvel4 = random.randint(-3,3)
    yvel4 != 0
    ballcolor4 = pygame.color.Color('deep pink')

    wincolor = pygame.color.Color("steel blue")
    
    ## ---------------------------------------------------------------------
    ##   Main Game Loop
    ## ---------------------------------------------------------------------

    keepGoing = True    
    while (keepGoing):

        
        pygame.time.delay(5)
        
        ## Handle events.  Here we check whether somebody clicked the
        ## 'X' in the upper right hand corner of the pygame window.
        ## We'll see more uses of events later.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        ## -----------------------------------------------------------------
        ##   Update Game State
        ## -----------------------------------------------------------------
                
        ballx = ballx+xvel
        bally = bally+yvel

        balla = balla+xvel2
        ballb = ballb+yvel2

        ballm = ballm+xvel3
        balln = balln+yvel3

        ballp = ballp+xvel4
        ballq = ballq+yvel4
        
        #this code makes the first ball bounce
        if (width - ballx <= ballr) or (ballx - ballr <= 0):
            xvel = -xvel
            score += 1
        if (height - bally <= ballr) or (bally - ballr <= 0):
            yvel = -yvel
            score += 1
            
        #this code makes the second ball bounce
        if (width - balla <= ballr2) or (balla - ballr2 <= 0):
            xvel2 = -xvel2
        if (height - ballb <= ballr2) or (ballb - ballr2 <= 0):
            yvel2 = -yvel2

        #this code changes the color of the first ball
        if ballcolor == pygame.color.Color('#99FF99') and ((width - ballx <= ballr) or (height - bally <= ballr) or (ballx - ballr <= 0) or (bally - ballr <= 0)):
            ballcolor = pygame.color.Color('saddle brown')
        elif ballcolor == pygame.color.Color('saddle brown') and ((width - ballx <= ballr) or (height - bally <= ballr) or (ballx - ballr <= 0) or (bally - ballr <= 0)):
            ballcolor = pygame.color.Color('#99FF99')
            
       #this code changes the color of the second ball
        if ballcolor2 == pygame.color.Color('firebrick') and ((width - balla <= ballr2) or (height - ballb <= ballr2) or (balla - ballr2 <= 0) or (ballb - ballr2 <= 0)):
            ballcolor2 = pygame.color.Color('#FFFF99')
            wincolor = pygame.color.Color('#4B0082')
        elif ballcolor2 == pygame.color.Color('#FFFF99') and ((width - balla <= ballr2) or (height - ballb <= ballr2) or (balla - ballr2 <= 0) or (ballb - ballr2 <= 0)):
            ballcolor2 = pygame.color.Color('firebrick')
            wincolor = pygame.color.Color('steel blue')

        #ball3
        #right side 
        if (width - ballm <= ballr3):
            ballr3 = random.randint(10,30)
            ballm = 1 + ballr3
        #left side
        if (ballm - ballr3 <= 0):
            ballr3 = random.randint(10,30)
            ballm = width - ballr3
        #bottom side
        if (height - balln <= ballr3):
            ballr3 = random.randint(10,30)
            balln = 1 + ballr3
        #top side
        if (balln - ballr3 <= 0):
            ballr3 = random.randint(10,30)
            balln = height - ballr3

        #ball4
        #right side 
        if (width - ballp <= ballr4):
            ballr4 = random.randint(10,30)
            ballp = 1 + ballr4
        #left side
        if (ballp - ballr4 <= 0):
            ballr4 = random.randint(10,30)
            ballp = width - ballr4
        #bottom side
        if (height - ballq <= ballr4):
            ballr4 = random.randint(10,30)
            ballq = 1 + ballr4
        #top side
        if (ballq - ballr4 <= 0):
            ballr4 = random.randint(10,30)
            ballq = height - ballr4


        ## -----------------------------------------------------------------
        ##   Draw Game State
        ## -----------------------------------------------------------------

        ## Erase the background
        my_win.fill(wincolor)
        
        ##   Draw ball
        pygame.draw.circle(my_win, ballcolor, (ballx, bally), ballr)
        
        pygame.draw.circle(my_win, ballcolor2, (balla, ballb), ballr2)

        pygame.draw.circle(my_win, ballcolor3, (ballm, balln), ballr3)

        pygame.draw.circle(my_win, ballcolor4, (ballp, ballq), ballr4)

        ##   Displays score.  Currently 0.
        font = pygame.font.SysFont("monospace", 20)
        StringScore = str(score)
        score_display = font.render("Score: " + StringScore,0, (255,255,255))
        my_win.blit(score_display, (20, 20))

        ## Show the pygame window.
        pygame.display.update()
        
        ## The game loop ends here.

    ## This closes your pygame window after we have left the game
    ## loop, i.e., after somebody closed the window.
    pygame.quit()


## Call the function run_game.
run_game()
