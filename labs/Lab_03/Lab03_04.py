#Programmer: Dani Massa

## lab3.py
## Author: Matthew Anderson
## Edits: John Rieffel
## Version: Windter 2020


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

    #ball1
    ballr = 30
    ballx = random.randint(0+ballr,width-ballr)
    bally = random.randint(0+ballr,height-ballr)
    xvel = random.randint(-3,3)
    xvel != 0
    yvel = random.randint(-3,3)
    yvel != 0
    ballcolor = pygame.color.Color('green')

    '''
    this program prevents the two circles from spawning with overlap.

    the while loop spawns the second circle at a random position, and tests to see if the two circles
    overlap by using the distance formula. If there is overlap, the loop sets the variable DifferentPosition to
    False, and then respawns the position of the first ball.
    '''
    DifferentPosition = True 
    while (DifferentPosition == True):
        #ball2
        ballr2 = 30
        balla = random.randint(0+ballr2,width-ballr2)
        ballb = random.randint(0+ballr,height-ballr)
        xvel2 = random.randint(-3,3)
        xvel2 != 0
        yvel2 = random.randint(-3,3)
        yvel2 != 0
        ballcolor2 = pygame.color.Color('pink')

        sumRadii = ballr +ballr2
        distance = math.sqrt ((ballx - balla)**2 + (bally - ballb)**2)
        
        if (distance < sumRadii):
            DifferentPosition = False
            ballx = random.randint(0+ballr,width-ballr)
            bally = random.randint(0+ballr,height-ballr)
        else:
            DifferentPosition = True
    
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
        
        #this code makes the ball bounce: it switches the direction of the velocity
        #when the ball hits the edges of the screen
        if (width - ballx <= ballr) or (ballx - ballr <= 0):
            xvel = -xvel
        if (height - bally <= ballr) or (bally - ballr <= 0):
            yvel = -yvel

        #this code changes the ball's color everytime it hits the edge of the screen
        if ballcolor == pygame.color.Color('green') and ((width - ballx <= ballr) or (height - bally <= ballr) or (ballx - ballr <= 0) or (bally - ballr <= 0)):
            ballcolor = pygame.color.Color('blue')
        elif ballcolor == pygame.color.Color('blue') and ((width - ballx <= ballr) or (height - bally <= ballr) or (ballx - ballr <= 0) or (bally - ballr <= 0)):
            ballcolor = pygame.color.Color('green')

        #this code makes the second ball wrap, change size and color.
        #right
        if (width - balla <= ballr2):
            ballr2 = random.randint(10,50)
            if (ballr2 > ballr):
                ballcolor2 = pygame.color.Color('white')
            else:
                ballcolor2 = pygame.color.Color('pink')
            balla = 1 + ballr2
            
        #left
        if (balla - ballr2 <= 0):
            ballr2 = random.randint(10,50)
            if (ballr2 > ballr):
                ballcolor2 = pygame.color.Color('white')
            else:
                ballcolor2 = pygame.color.Color('pink')
            balla = width - ballr2
           
        #bottom
        if (height - ballb <= ballr2):
            ballr2 = random.randint(10,50)
            if (ballr2 > ballr):
                ballcolor2 = pygame.color.Color('white')
            else:
                ballcolor2 = pygame.color.Color('pink')
            ballb = 1 + ballr2
            
        #top
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


