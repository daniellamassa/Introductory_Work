## Programmer: Dani Massa
## Author: Matthew Anderson
## Edits: John Rieffel
## Version: Windter 2020

'''
This program spawns 75 balls with random positions, velocities, sizes, and colors. When the balls bounce off the edge
of the screen, the score is increased by 1.
'''

import pygame
import random

# The following function makes each ball. I added and subtracted 10 from the x and y coordinates to prevent the
# ball from spawning on the edge of the screen and getting stuck.

def MakeBall (height, width):
        (x,y) = (random.randint(10, (width-10)), random.randint(10, (height-10)))
        r = random.randint(1,10)
        (xv, yv) = (random.randint(-5, 5), random.randint(-5, 5))
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        c = (red, green, blue)
        Ball = [(x, y), r, (xv,yv), c]
        return Ball
# The following 3 functions return the random values of red, green and blue of each ball. I had to create 3 separate
# functions for the color in order to pass the values into the .Color pygame function correctly (3 arguements, not 1 tuple)

def GetRed(List):
        color = List[3]
        red = color[0]
        return red

def GetGreen(List):
        color = List[3]
        green = color[1]
        return green

def GetBlue(List):
        color = List[3]
        blue = color[2]
        return blue

# The following function returns the position of a given ball.

def GetPos(List):
        pos = List[0]
        return pos

# The following function returns the radius of a given ball.

def GetRadius(List):
        radius = List[1]
        return radius

# The following function updates the balls position so that it moves. At first when I tried to add the tuples together it returned
# a 4-length tuple instead of adding the values together and keeping the length 2. I realized I needed to specify the indexs when
# adding, and create a whole new tuple with the new values.

def UpdatePos(List):
        position = List[0]
        velocity = List[2]
        NewPositionX = (position[0]) + (velocity[0])
        NewPositionY = (position[1]) + (velocity[1])
        NewPosition = (NewPositionX, NewPositionY)
        List[0] = NewPosition
        return List
        

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

    b1 = MakeBall(height,width)
    b2 = MakeBall(height,width)
    b3 = MakeBall(height,width)
    b4 = MakeBall(height,width)

    ballList = [b1, b2, b3, b4]

    # The following code makes 75 balls, and adds each ball to the ballList.
    
    BallCount = 4
    while BallCount < 76:
            b = MakeBall(height, width)
            ballList.append(b)
            BallCount += 1
    
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

        #This for loop makes the balls bounce. I used my old code from the previous lab that made the balls bounce, but I had to
        # substitute specific indexs for the positions, velocities, and radii.
        
        for curBall in ballList:
                curBall = UpdatePos(curBall)
                BallPosition = curBall[0]
                BallX = (BallPosition[0])
                BallY = (BallPosition[1])
                BallVelocity = curBall[2]
                xVel = (BallVelocity[0])
                yVel = (BallVelocity[1])
                if (width - BallX <= curBall[1]) or (BallX - curBall[1] <= 0):
                        xVel = -xVel
                        score += 1
                if (height - BallY <= curBall[1]) or (BallY - curBall[1] <= 0):
                        yVel = -yVel
                        score += 1
                NewVelocity = (xVel, yVel)
                curBall[2] = NewVelocity
                        
        ## -----------------------------------------------------------------
        ##   Draw Game State
        ## -----------------------------------------------------------------

        ## Erase the background
        my_win.fill(pygame.color.Color("black"))
        
        ##   Draw ball
        for curBall in ballList:
              pygame.draw.circle(my_win, pygame.Color(GetRed(curBall), GetGreen(curBall), GetBlue(curBall)), GetPos(curBall), GetRadius(curBall))     

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
