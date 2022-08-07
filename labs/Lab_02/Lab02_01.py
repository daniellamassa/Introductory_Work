## Programmer: Dani Massa

## Author: Kristina Striegnitz
## Edited: Matthew Anderson
##
## Version: Spring 2019
##
## This program draws some colored geometric shapes using built-in
## pygame functions.
##
## Everything following a '#' is a 'comment'. Comments are
## explanations for the programmer or other human beings looking at
## the code. The Python interpreter ignores them.  All lines that do
## not start with a '#', are instructions for the Python interpreter.

## Load the pygame and time libraries, so that we can use the functionality it
## provides.

import pygame, time

## This function defines our whole "game", which is a very simple
## game. All it does is display a picture.

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    ## Open the pygame window with the specified width and height. We
    ## call our pygame window 'my_win'.
    
    width = 640
    height = 480
    my_win = pygame.display.set_mode((width,height))
    EndpointX = 550
    EndpointY = 200


    ## This is the "game loop". We will talk much more about the game
    ## loop later. For now: the game loop keeps the pygame window on
    ## the screen until you click the 'X' in the upper right hand
    ## corner.

    keepGoing = True    
    while (keepGoing):

        ## Handle events.  Here we check whether somebody clicked the
        ## 'X' in the upper right hand corner of the pygame window.
        ## We'll see more uses of events later.
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        ## Create and show graphics.

        ## Make the background black.
        ##
        ##   We specify colors using the expression
        ##   'pygame.color.Color(<Color Name>)', where '<Color Name>'
        ##   needs to be replaced by an actual color name in
        ##   quotes. (Note 1: The quotes are important. Note 2: I will
        ##   always use angular brackets for places where you need to
        ##   substitute in an expression.)  For more supported color
        ##   names, look at the table of X11 colors on this page:
        ##   http://en.wikipedia.org/wiki/Web_colors. (Note: for
        ##   pygame all letters need to be lower case.)

        my_win.fill(pygame.color.Color("light blue"))

        ## Compose a picture from shapes.
        ## Draw two rectangles.
        ##
        ##   We specify where we want to draw it by giving the name of
        ##   our pygame window - 'my_win'.  We specify a color (as
        ##   described above).  We specify where in the window to put
        ##   the rectangles. This is done by giving a tuple of four
        ##   numbers. The third number specifies the width of the
        ##   rectangle and the fourth number specifies the height.
        ##   The first two numbers specify the x-coordinate and the
        ##   y-coordinate of the upper left hand corner of the
        ##   rectangle. The origin of the coordinate system is in the
        ##   upper left hand corner of the pygame window. x values
        ##   increase going from the left to right; y values increase
        ##   going from top to bottom.
        
        pygame.draw.rect(my_win, pygame.color.Color('white'), (100,100,50,50))
        pygame.draw.rect(my_win, pygame.color.Color('darkmagenta'), (140,140,70,40))

        ## Draw a circle.
        ##
        ##   We specify the window, the color, the position (x and y
        ##   coordinates) of the center, and the radius.
        
        pygame.draw.circle(my_win, pygame.color.Color('navy'), (width-75, height-75),75)
        pygame.draw.circle(my_win, pygame.color.Color('red'), (EndpointX, EndpointY),37)

        ## Draw a line.
        ##
        ##   We specify the window, the color, the starting point and
        ##   the ending point of the line.
        
        pygame.draw.line(my_win,pygame.color.Color('orange'),(50,320),(550,200))
        
        ## Draw a polygon.
        ##
        ##   We specify the window, the color, and a list of points -
        ##   each points represents one corner.
        
        pygame.draw.polygon(my_win,pygame.color.Color('darkgreen'), \
                            [(150,300),(150+120,300),(150+60,300+120)])

        pygame.draw.line(my_win,pygame.color.Color('black'),(450,50),(550,50))
        pygame.draw.line(my_win,pygame.color.Color('black'),(450,100),(550,100))
        pygame.draw.line(my_win,pygame.color.Color('black'),(483,25),(483,135))
        pygame.draw.line(my_win,pygame.color.Color('black'),(517,25),(517,135))


        ## Show the pygame window.
        
        pygame.display.update()
        
        ## The game loop ends here.

    ## This closes your pygame window after we have left the game
    ## loop, i.e., after somebody closed the window.
    pygame.quit()


## Call the function run_game.

run_game()
