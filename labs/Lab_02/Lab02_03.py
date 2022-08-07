#Programmer: Dani Massa
#the code relating to the def run_game() and the while loop were created by
#Proffesor Kristina Striegnitz and edited by Matthew Anderson

import pygame, time

def run_game():

    pygame.init()

    width = 800
    height = 800
    my_win = pygame.display.set_mode((width,height))
    frame_num = 0

    keepGoing = True    
    while (keepGoing):
        frame_num += 1        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        my_win.fill(pygame.color.Color("black"))
        #these white rectangles are perfectly aligned with every other circle in the program
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,50,800,60))
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,130,800,60))
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,210,800,60))
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,290,800,60))
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,370,800,60))
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,450,800,60))
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,530,800,60))
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,610,800,60))
        pygame.draw.rect(my_win, pygame.color.Color('white'), (0,690,800,60))

        pygame.draw.circle(my_win, pygame.color.Color('firebrick'), (40+(frame_num//4),40), 30)
        pygame.draw.circle(my_win, pygame.color.Color('orange red'), (760-(frame_num//4),80), 30)
        pygame.draw.circle(my_win, pygame.color.Color('dark orange'), (40+(frame_num//4),120), 30)
        pygame.draw.circle(my_win, pygame.color.Color('gold'), (760-(frame_num//4),160), 30)
        pygame.draw.circle(my_win, pygame.color.Color('lawn green'), (40+(frame_num//4),200), 30)
        pygame.draw.circle(my_win, pygame.color.Color('green'), (760-(frame_num//4),240), 30)
        pygame.draw.circle(my_win, pygame.color.Color('dark green'), (40+(frame_num//4),280), 30)
        pygame.draw.circle(my_win, pygame.color.Color('dark cyan'), (760-(frame_num//4),320), 30)
        pygame.draw.circle(my_win, pygame.color.Color('medium blue'), (40+(frame_num//4),360), 30)
        pygame.draw.circle(my_win, pygame.color.Color('dodger blue'), (760-(frame_num//4),400), 30)
        pygame.draw.circle(my_win, pygame.color.Color('#4B0082'), (40+(frame_num//4),440), 30)
        pygame.draw.circle(my_win, pygame.color.Color('#800080'), (760-(frame_num//4),480), 30)
        pygame.draw.circle(my_win, pygame.color.Color('medium violet red'), (40+(frame_num//4),520), 30)
        pygame.draw.circle(my_win, pygame.color.Color('deep pink'), (760-(frame_num//4),560), 30)
        pygame.draw.circle(my_win, pygame.color.Color('hot pink'), (40+(frame_num//4),600), 30)
        pygame.draw.circle(my_win, pygame.color.Color('pink'), (760-(frame_num//4),640), 30)
        pygame.draw.circle(my_win, pygame.color.Color('wheat'), (40+(frame_num//4),680), 30)
        pygame.draw.circle(my_win, pygame.color.Color('#AC7D4E'), (760-(frame_num//4),720), 30)
        pygame.draw.circle(my_win, pygame.color.Color('#C0C0C0'), (40+(frame_num//4),760), 30)

                         
        pygame.display.update()

    pygame.quit()

run_game()
