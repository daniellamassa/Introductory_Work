##
## Author: Kristina Striegnitz
##
## Version: Fall 2012
##
## This program shows the image of a little boxy guy. Your task is to
## use the other images provided to animate the image such that the
## guy seems to walk.

import pygame

width = 640
height = 480
my_win = pygame.display.set_mode((width,height))

def draw_background():
    background_img = pygame.image.load('background.png').convert()
    background_img = pygame.transform.scale(background_img, (width, height)) 
    my_win.blit(background_img, (0, 0))

def MakeListOfGuys():
    guys = []
    fnames = ["WalkingSquare1.bmp","WalkingSquare2.bmp","WalkingSquare3.bmp","WalkingSquare4.bmp","WalkingSquare5.bmp"]
    for name in fnames:
        guy = pygame.image.load(name)
        bgcolor = guy.get_at((0,guy.get_height()-1)) #find the color of the bottom left right corner
        guy.set_colorkey(bgcolor) #set that color to translucent
        guy = guy.convert()
        guys.append(guy)
    return guys

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.
    pygame.init()



    guys = MakeListOfGuys()
    counter = 0
    counting = False
    number = 0

    # Load an image and convert it to pygame's internal image
    # format. The result is an image object wwhich is in a box labeled
    # 'guy'.
    guy = pygame.image.load("WalkingSquare1.bmp")
    gw = guy.get_width()
    gh = guy.get_height()
  
    bgcolor = guy.get_at((0,gh-1)) #find the color of the bottom left right corner
    guy.set_colorkey(bgcolor) #set that color to translucent
    guy = guy.convert()

    # initialize the guy's position and speed
    x = width/2
    y = 335
    x_v = 0
    y_v = 0

    ## The game loop starts here.
   
    keepGoing = True    
    while (keepGoing):

        movement = 0
        ## Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
            elif event.type == pygame.KEYDOWN:

                # Key pressed event
                key_pressed = event.dict['key']
                print("Key pressed = %s" % key_pressed)

                #right movement
                if key_pressed == (275):
                    x_v = 5
                    counting = True
                    
                #left movement
                if key_pressed == (276):
                   x_v = -5
                   counting = True
                    
            elif event.type == pygame.KEYUP:

                # Key released event
                key_released = event.dict['key']
                print("Key released = %s" % key_released)
                
                if key_released == (275) or key_released == (276):
                    x_v = 0
                    counting = False
                    
        # Prevents sprite from traveling offscreen
        if x + x_v > width - gw:
            x_v = 0
        if x + x_v < 0:
            x_v = 0

        ## Simulate game world
        x += x_v
        y += y_v

        ## Draw picture and update display

        draw_background()

        # Animates the sprite
        
        if (counting == True):
            number += 0.10
        counter = int(number)
        guyindex = counter % 5

        curguy = guys[guyindex]
        flippedguy = pygame.transform.flip(curguy, True, False)
            
        if (x_v ==  5):
            curguy = guys[guyindex]

        if (x_v == -5):
            curguy = flippedguy
            
            
        # put image in the picture at the desired location x, y
        my_win.blit(curguy,(x,y))

        pygame.display.update()

        
        
    ## The game loop ends here.

    pygame.quit()


## Call the function run_game.

run_game()
