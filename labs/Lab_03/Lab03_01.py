# Programmer: Dani Massa

## lab3.py
## Author: Matthew Anderson
## Edits: John Rieffel
## Version: Windter 2020

'''
This program spawns a green circle at a random location with a random velocity, and
has it move down and towards the right. Unfortunately if the circle spawns close to the
lower right hand corner it dissapears fairly quickly. 
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

    # this code sets the ball's radius, it's location to a random coordinate, and
    # the ball's velocity to a random integer
    ballr = 20
    ballx = random.randint(0+ballr,width-ballr)
    bally = random.randint(0+ballr,height-ballr)
    xvel = random.randint(1,3)
    yvel = random.randint(1,3)

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

        #this code makes the ball move. By using addition (and positive integers for
        #the velocity) the ball moves down and to the right. 
        ballx = ballx+xvel
        bally = ballx+yvel

        ## -----------------------------------------------------------------
        ##   Draw Game State
        ## -----------------------------------------------------------------

        ## Erase the background
        my_win.fill(pygame.color.Color("black"))
        
        ##   Draw ball
        pygame.draw.circle(my_win, pygame.color.Color('green'), (ballx, bally), ballr)        

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
