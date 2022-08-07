#Programmer: Dani Massa

## lab3.py
## Author: Matthew Anderson
## Edits: John Rieffel
## Version: Windter 2020

'''
this program adds a second ball that wraps around the screen,
and changes sizes once it reappears. if this ball is smaller than
the first ball it is pink, and if it is larger it is white.
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

    # this code pertains to the first ball
    ballr = 30
    ballx = random.randint(0+ballr,width-ballr)
    bally = random.randint(0+ballr,height-ballr)
    xvel = random.randint(-3,3)
    xvel != 0
    yvel = random.randint(-3,3)
    yvel != 0
    ballcolor = pygame.color.Color('green')

    # this code pertains to the second ball
    ballr2 = 20
    balla = random.randint(0+ballr2,width-ballr2)
    ballb = random.randint(0+ballr,height-ballr)
    xvel2 = random.randint(-3,3)
    xvel2 != 0
    yvel2 = random.randint(-3,3)
    yvel2 != 0
    ballcolor2 = pygame.color.Color('pink')
        
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
                
        # This code makes both balls move by adding velocity
        ballx = ballx+xvel
        bally = bally+yvel

        balla = balla+xvel2
        ballb = ballb+yvel2
        
        # this code makes the ball bounce: it switches the direction of the velocity
        # when the ball hits the edges of the screen
        if (width - ballx <= ballr) or (ballx - ballr <= 0):
            xvel = -xvel
        if (height - bally <= ballr) or (bally - ballr <= 0):
            yvel = -yvel

        # this code changes the ball's color everytime it hits the edge of the screen
        if ballcolor == pygame.color.Color('green') and ((width - ballx <= ballr) or (height - bally <= ballr) or (ballx - ballr <= 0) or (bally - ballr <= 0)):
            ballcolor = pygame.color.Color('blue')
        elif ballcolor == pygame.color.Color('blue') and ((width - ballx <= ballr) or (height - bally <= ballr) or (ballx - ballr <= 0) or (bally - ballr <= 0)):
            ballcolor = pygame.color.Color('green')

        '''
        the following code makes the second ball wrap around the screen, change size and color.

        each if statements pertains to one side of the screen. Originally I had my if statements simply change
        the position of balla and ballb by setting them to 0 or the height/width, however then my if statements began to
        conflict with each other so I had to add the addition/subtraction of the radius.

        the ballr2 = random.rabdint changes the size.

        the if/else statements check the size of the second bal compared to the first ball, and then adjusts its color accordingly.
        
        '''
        #right side
        if (width - balla <= ballr2):
            ballr2 = random.randint(10,50)
            if (ballr2 > ballr):
                ballcolor2 = pygame.color.Color('white')
            else:
                ballcolor2 = pygame.color.Color('pink')
            balla = 1 + ballr2
            
        #left side
        if (balla - ballr2 <= 0):
            ballr2 = random.randint(10,50)
            if (ballr2 > ballr):
                ballcolor2 = pygame.color.Color('white')
            else:
                ballcolor2 = pygame.color.Color('pink')
            balla = width - ballr2
           
        #bottom side
        if (height - ballb <= ballr2):
            ballr2 = random.randint(10,50)
            if (ballr2 > ballr):
                ballcolor2 = pygame.color.Color('white')
            else:
                ballcolor2 = pygame.color.Color('pink')
            ballb = 1 + ballr2
            
        #top side
        if (ballb - ballr2 <= 0):
            ballr2 = random.randint(10,50)
            if (ballr2 > ballr):
                ballcolor2 = pygame.color.Color('white')
            else:
                ballcolor2 = pygame.color.Color('pink')
            ballb = height - ballr2
            

        ## -----------------------------------------------------------------
        ##   Draw Game State
        ## -----------------------------------------------------------------

        ## Erase the background
        my_win.fill(pygame.color.Color("black"))
        
        ##   Draw ball
        pygame.draw.circle(my_win, ballcolor, (ballx, bally), ballr)
        # draws the second ball
        pygame.draw.circle(my_win, ballcolor2, (balla, ballb), ballr2)

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
