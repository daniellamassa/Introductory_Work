# space.py
import pygame, time, random
# A basic space game.
# Author: Matthew Anderson
# Version: Fall 2017


## ----------------------------------------------------------------------
##     Initialize Global Variables
## ----------------------------------------------------------------------

## Initialize the pygame submodules and set up the display window.
pygame.init()

# Global variables for the window.
WIDTH = 640
HEIGHT = 480
RADIUS = 10
MY_WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Global variables containing properties of the ship and lasers
SHIP_DY = 5
LASER_DX = 5
SCORE = 0

## ----------------------------------------------------------------------
##     Helper Functions
## ----------------------------------------------------------------------

def collide(circ1, circ2):
    '''
    circ1 and circ2 are tuples of the form ((x,y),radius)) that
    describe circles.  This function returns True if the circles
    are overlaping and False otherwise.

    This is code from Lab 4
    '''

    ((x1, y1), r1) = circ1
    ((x2, y2), r2) = circ2

    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    result = d <= r1 + r2

    return result  

## ----------------------------------------------------------------------
##     Ship Functions
## ----------------------------------------------------------------------

# This function adds a laser to the ship and prevents it from going offscreen.
def fire_laser(lasers, ship):

    # Add a laser at the ship's location.
    lasers.append(ship)

# This function allows for ship movement upwards.
def move_ship_up(ship):

    (sx, sy) = ship
    sy = sy - SHIP_DY
    # Prevent the ship from going off the top of the screen.
    if sy < 0:
        sy = 0

    return (sx,sy)

# This function allows for ship movement downwards.
def move_ship_down(ship):

    global HEIGHT

    (sx, sy) = ship
    # Prevent the ship from going off the bottom of the screen.
    sy = sy + SHIP_DY
    if sy > HEIGHT:
        sy = HEIGHT

    return (sx,sy)

# This function creates the ship.
def draw_ship(ship):

    global MY_WIN # Need to access the global variable for the window to draw

    # Unpack the coordinates of the ship
    (sx, sy) = ship
    # Determine the outline of the ship
    #outline = [(sx + 10, sy), (sx - 10, sy - 10),(sx - 10, sy + 10)]
    # Draw the ship
    #pygame.draw.polygon(MY_WIN, pygame.color.Color('blue'), outline)
    ship_img = pygame.image.load('SpaceShip.png').convert()
    ship_img = pygame.transform.scale(ship_img, (40,40)) 
    MY_WIN.blit(ship_img, (sx-20, sy-20))

## ----------------------------------------------------------------------
##     Laser Functions
## ----------------------------------------------------------------------

def draw_lasers(lasers):
    '''Displays all the lasers as white circles.'''

    global MY_WIN
    global RADIUS

    # Loop over the lasers.
    for laser in lasers:
        # Unpack the laser
        (bx, by) = laser
        # Draw the laser
        LaserRadius = int((RADIUS + bx*0.05)//1) 
        
        pygame.draw.circle(MY_WIN, pygame.color.Color('white'), (bx, by), LaserRadius)


def move_lasers(lasers):
    '''Moves all the lasers to the right by LASER_DX, removes lasers that go out of the window.'''

    global LASER_DX
    global RADIUS
    global WIDTH

    # Make an empty list to store the updated lasers.
    new_lasers = []
    # Loop over the lasers moving them.
    for laser in lasers:        
        # Unpack the laser.
        (bx, by) = laser
        # Move the laser to the right.
        bx = bx + LASER_DX
        # Appends to list of remaining lasers if still on screen
        if bx <= WIDTH + RADIUS:
            new_lasers.append((bx, by))

    return new_lasers

## ----------------------------------------------------------------------
##     World Functions
## ----------------------------------------------------------------------

def draw_background():
    '''Displays the background by filling with black.'''

    global MY_WIN
    background_img = pygame.image.load('space.bmp').convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT)) 
    MY_WIN.blit(background_img, (0, 0))

    # MY_WIN.fill(pygame.color.Color("black"))


def draw_score():
    '''Displays the score.'''

    global SCORE
    global MY_WIN
    global WIDTH

    font = pygame.font.SysFont("monospace", 20)
    score_display = font.render("Score: %d" % SCORE, 0, (255, 255, 255))
    MY_WIN.blit(score_display, (WIDTH - 150, 20))

## ----------------------------------------------------------------------
##     Alien Functions
## ----------------------------------------------------------------------

def move_alien(alien):
    '''
    Moves one alien. 
    Returns the (x,y) position the alien moves to. 
    '''

    (ax, ay) = alien

    NewPositionX = random.randint (-2, 2)
    NewPositionY = random.randint (-2, 2)
    NewTuple = ((ax + NewPositionX), (ay + NewPositionY))

    ## Return the new position.

    return (NewTuple)

def move_aliens(aliens):
    '''Moves all aliens.'''
    
    for i in range(len(aliens)):
        aliens[i] = move_alien(aliens[i])    


def draw_alien(alien):
    '''Draws one alien as an exciting yellow square.'''

    global MY_WIN
    global RADIUS
    (sx, sy) = alien
    # Determine the outline of the alien
    outline = [(sx + 10, sy + 10), (sx + 10, sy - 10), (sx - 10, sy - 10),(sx - 10, sy + 10)]
    
    pygame.draw.polygon(MY_WIN, pygame.color.Color('yellow'), (outline))


def draw_aliens(aliens):
    '''Draws all the aliens in the list.'''

    for alien in aliens:
        draw_alien(alien)


def remove_aliens(aliens, lasers):
    '''Compares a list of aliens and lasers and removes lasers and
    aliens which collide.  Returns a tuple containing the updated
    lists of aliens and lasers.  
    Bug: Doesn't update the score.
    '''

    global RADIUS
    global SCORE

    new_aliens = []

    # Note: This code is complicated.  You could figure out how it
    # works, but that's not necessary for lab.
    
    for alien in aliens:
        collided = False
        for laser in lasers:
            (bx, by) = laser
            LaserRadius = int((RADIUS + bx*0.05)//1) 
            if collide((alien, RADIUS), (laser, LaserRadius)):
                print("Hit Alien!")
                collided = True
                break

        if collided:
            lasers.remove(laser)
            SCORE += 1
        else:
            new_aliens.append(alien)

    return (new_aliens, lasers)


def add_aliens(aliens):
    '''Adds one alien to the list of aliens at a random position.
    Changed from 1/100 chance of spawning to 1/10 chance. Returns None.'''

    global HEIGHT
    global WIDTH

    if random.randint(0, 10) == 0:
        aliens.append((random.randint(100, WIDTH), random.randint(0, HEIGHT)))


## ----------------------------------------------------------------------
##     Main Game Loop
## ----------------------------------------------------------------------

def update_game(aliens, firing, lasers, ship):
    add_aliens(aliens)


    if firing:
        fire_laser(lasers, ship)

    lasers = move_lasers(lasers)
    move_aliens(aliens)

    # Remove aliens hit by lasers
    (aliens, lasers) = remove_aliens(aliens, lasers)

    return (aliens, lasers)

def run_game():
     
    FPS = 300
    
    # Initialize objects in game: ship, lasers, aliens
    global ship 
    ship = (50, 240)
    lasers = []
    aliens = []

    frame = 0

    has_won = False

    firing = False
    movement = 0
    q = False
    p = False

    ## Load other resources
    pygame.mixer.music.load("mario_bros_trimmed.ogg")
    pygame.mixer.music.play(-1)
    
    while (not has_won) and (q == False):

        frame += 1  
        ## Sleep so that the frames come at even intervals.
        time.sleep(1.0/FPS)

        ## ====================================================
        ##   Handle Events
        ## ====================================================

        events = pygame.event.get()
        #print events
        for event in events:
            #print "Type = ", event.type
            if event.type == pygame.QUIT:

                # Window close event -- Stop game!
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:

                # Key pressed event
                key_pressed = event.dict['key']
                print("Key pressed = %s" % key_pressed)

                if key_pressed == (113):
                    q = True

                if key_pressed == (112):
                    p = not p

                if key_pressed == (1073741906):
                    #ship = move_ship_up(ship)
                    movement = 1
                    
                elif key_pressed == (1073741905):
                    #ship = move_ship_down(ship)
                    movement = 2
                    
                elif key_pressed == ord(" "):
                    firing = True
                    
            elif event.type == pygame.KEYUP:

                # Key released event
                key_released = event.dict['key']
                print("Key released = %s" % key_released)
                
                if key_released == ord(" "):
                    firing = False

                if key_released == (1073741906) or key_released == (1073741905):
                    movement = 0

        ## ====================================================
        ##   Update Game
        ## ====================================================
        
        if (p == False):
            (aliens, lasers) = update_game(aliens, firing, lasers, ship)
            
            if movement == 1:
                ship = move_ship_up(ship)
            elif movement == 2:
                ship = move_ship_down(ship)
             
            
        ## ====================================================
        ##   Display Game
        ## ====================================================

        ## Draw the objects in the game.
        draw_background()
        draw_lasers(lasers)
        draw_aliens(aliens)
        draw_ship(ship)
        draw_score()

        ## Show the pygame window.       
        pygame.display.update()
        
        ## The game loop ends here.

    ## This closes your pygame window after we have left the game
    ## loop, i.e., after somebody closed the window.
    pygame.quit()


## Call the function run_game.

run_game()
