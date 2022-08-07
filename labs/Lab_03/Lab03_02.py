# Programmer: Dani Massa

## lab3.py
## Author: Matthew Anderson
## Edits: John Rieffel
## Version: Windter 2020

'''
This program generates a bouncing ball that changes color everytime
it hits the edge of the screen.
'''

import pygame
import random


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
    
    ballr = 20
    ballx = random.randint(0+ballr,width-ballr)
    bally = random.randint(0+ballr,height-ballr)
    xvel = random.randint(-3,3)
    xvel != 0
    yvel = random.randint(-3,3)
    yvel != 0

    # this line of code creates a variable for the ball's color, which
    # will be manipulated using if statements
    ballcolor = pygame.color.Color('green')
        
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
        
        # this code makes the ball bounce by testing to see if it hits the edge,
        # and then changes the direction of it's velocity
        if (width - ballx <= ballr) or (ballx - ballr <= 0):
            xvel = -xvel
        if (height - bally <= ballr) or (bally - ballr <= 0):
            yvel = -yvel

        #this code changes the ball's color
        #the 4 expressions with the 'or' operator represent the 4 sides of the screen
        if ballcolor == pygame.color.Color('green') and ((width - ballx <= ballr) or (height - bally <= ballr) or (ballx - ballr <= 0) or (bally - ballr <= 0)):
            ballcolor = pygame.color.Color('blue')
        elif ballcolor == pygame.color.Color('blue') and ((width - ballx <= ballr) or (height - bally <= ballr) or (ballx - ballr <= 0) or (bally - ballr <= 0)):
            ballcolor = pygame.color.Color('green')

        ## -----------------------------------------------------------------
        ##   Draw Game State
        ## -----------------------------------------------------------------

        ## Erase the background
        my_win.fill(pygame.color.Color("black"))
        
        ##   Draw ball
        # the variable "ballcolor" had to be inputted into the drawing of the circle 
        pygame.draw.circle(my_win, ballcolor, (ballx, bally), ballr)

        ##   Displays score.  Currently 0.
        font = pygame.font.SysFont("monospace", 20)
        score_display = font.render("Score: 0", 0, (255,255,255))
        my_win.blit(score_display, (20, 20))

        ## Show the pygame window.
        pygame.display.update()
        
        ## The game loop ends here.

    ## This closes your pygame window after we have left the game
    ## loop, i.e., after somebody closed the window.
    pygame.quit()


## Call the function run_game.
run_game()
