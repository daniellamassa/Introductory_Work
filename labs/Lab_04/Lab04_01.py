# Programmer: Dani Massa

## lab4.py
## Author: Matthew Anderson
## Edits: John Rieffel
## Version: Windter 2020

import pygame
import random
import math


# this function tests to see if two balls collide, and returns a boolean value.

def Collide(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)
    collides = False
    if (distance < (r1 +r2)):
        collides = True
    return (collides)

# this function returns an area value for a given radius of a circle.

def Mass(r):
    a = math.pi * (r**2)
    return (a)
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

    #this code creates the variable for the score
    score = 0
        
    #ball1
    ballr = 30
    ballx = random.randint(0+ballr,width-ballr)
    bally = random.randint(0+ballr,height-ballr)
    xvel = random.randint(-3,3)
    xvel != 0
    yvel = random.randint(-3,3)
    yvel != 0
    ballcolor = pygame.color.Color('blue')

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
        ballcolor2 = pygame.color.Color('green')

        #ball3
        ballr3 = 60
        ballm = random.randint(0+ballr,width-ballr)
        balln = random.randint(0+ballr,height-ballr)
        xvel3 = random.randint(-3,3)
        xvel3 != 0
        yvel3 = random.randint(-3,3)
        yvel3 != 0
        ballcolor3 = pygame.color.Color('red')

        sumRadii = ballr +ballr2
        sumRadii2 = ballr + ballr3
        sumRadii3 = ballr2 +ballr3
        
        distance = math.sqrt ((ballx - balla)**2 + (bally - ballb)**2)
        
        if (distance < sumRadii) or (distance < sumRadii2):
            DifferentPosition = False
            ballx = random.randint(0+ballr,width-ballr)
            bally = random.randint(0+ballr,height-ballr)
        elif (distance < sumRadii3):
            balla = random.randint(0+ballr,width-ballr)
            ballb = random.randint(0+ballr,height-ballr)
        else:
            DifferentPosition = True
            
    # this code assigns the mass of each ball to a variable.
    ball1mass = Mass(ballr)
    ball2mass = Mass(ballr2)
    ball3mass = Mass(ballr3)
    
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
        
        # this code makes the three balls bounce off of all 4 edges of the screen.
        if (width - ballx <= ballr) or (ballx - ballr <= 0):
            xvel = -xvel
        if (height - bally <= ballr) or (bally - ballr <= 0):
            yvel = -yvel
        if (width - balla <= ballr2) or (balla - ballr2 <= 0):
            xvel2 = -xvel2
        if (height - ballb <= ballr2) or (ballb - ballr2 <= 0):
            yvel2 = -yvel2
        if (width - ballm <= ballr3) or (ballm - ballr3 <= 0):
            xvel3 = -xvel3
        if (height - balln <= ballr3) or (balln - ballr3 <= 0):
            yvel3 = -yvel3
            
        # the following code tests for collisions using if statements, and makes the balls bounce off of each other when they collide.
        # the code that is commented out makes the balls bounce off of each other when they have the same mass.
        # the following program also changes the score.
        
        if Collide(ballx, bally, ballr, balla, ballb, ballr2) == True:

            xvelprime = round(((ball1mass - ball2mass)/(ball1mass + ball2mass)*xvel) + ((2*ball2mass)/(ball1mass + ball2mass)*xvel2))
            xvel2 = round(((2*ball1mass)/(ball1mass + ball2mass)*xvel) + ((ball2mass - ball1mass)/(ball1mass + ball2mass)*xvel2))
            xvel = xvelprime
            yvelprime = round(((ball1mass - ball2mass)/(ball1mass + ball2mass)*yvel) + ((2*ball2mass)/(ball1mass + ball2mass)*yvel2))
            yvel2 = round(((2*ball1mass)/(ball1mass + ball2mass)*yvel) + ((ball2mass - ball1mass)/(ball1mass + ball2mass)*yvel2))
            yvel = yvelprime

##            xvelprime = xvel
##            xvel = xvel2
##            xvel2 = xvelprime
##            yvelprime = yvel
##            yvel = yvel2
##            yvel2 = yvelprime
            
        if Collide(ballx, bally, ballr, ballm, balln, ballr3) == True:
            
            xvelprime2 = round(((ball1mass - ball3mass)/(ball1mass + ball3mass)*xvel) + ((2*ball3mass)/(ball1mass + ball3mass)*xvel3))
            xvel3 = round(((2*ball1mass)/(ball1mass + ball3mass)*xvel) + ((ball3mass - ball1mass)/(ball1mass + ball3mass)*xvel3))
            xvel = xvelprime2
            yvelprime2 = round(((ball1mass - ball3mass)/(ball1mass + ball3mass)*yvel) + ((2*ball3mass)/(ball1mass + ball3mass)*yvel3))
            yvel3 = round(((2*ball1mass)/(ball1mass + ball3mass)*yvel) + ((ball3mass - ball1mass)/(ball1mass + ball3mass)*yvel3))
            yvel = yvelprime2
            
##            xvelprime2 = xvel
##            xvel = xvel3
##            xvel3 = xvelprime2
##            yvelprime2 = yvel
##            yvel = yvel3
##            yvel3 = yvelprime2
            
            score -= 1
            
        if Collide(balla, ballb, ballr2, ballm, balln, ballr3) == True:
            xvelprime3 = round(((ball2mass - ball3mass)/(ball2mass + ball3mass)*xvel2) + ((2*ball3mass)/(ball2mass + ball3mass)*xvel3))
            xvel3 = round(((2*ball2mass)/(ball2mass + ball3mass)*xvel2) + ((ball3mass - ball2mass)/(ball2mass + ball3mass)*xvel3))
            xvel2 = xvelprime3
            yvelprime3 = round(((ball2mass - ball3mass)/(ball2mass + ball3mass)*yvel2) + ((2*ball3mass)/(ball2mass + ball3mass)*yvel3))
            yvel3 = round(((2*ball2mass)/(ball2mass + ball3mass)*yvel2) + ((ball3mass - ball2mass)/(ball2mass + ball3mass)*yvel3))
            yvel2 = yvelprime3
            
##            xvelprime3 = xvel2
##            xvel2 = xvel3
##            xvel3 = xvelprime3
##            yvelprime3 = yvel2
##            yvel2 = yvel3
##            yvel3 = yvelprime3
            
            score += 2

        ## -----------------------------------------------------------------
        ##   Draw Game State
        ## -----------------------------------------------------------------

        ## Erase the background
        my_win.fill(pygame.color.Color("black"))
        
        ##   Draw ball
        pygame.draw.circle(my_win, ballcolor, (ballx, bally), ballr)
        
        pygame.draw.circle(my_win, ballcolor2, (balla, ballb), ballr2)

        pygame.draw.circle(my_win, ballcolor3, (ballm, balln), ballr3)

        ##   Displays score.  Currently 0.
        font = pygame.font.SysFont("monospace", 20)
        # this code creates a new varaible that changes the original score variable into a string
        # so it can be added to the score_display.
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
