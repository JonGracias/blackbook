# Imports
import os
import pickle
import sys
import pygame
import addict




def main():
    pygame.init()
    running = True


    while running: # main game loop


        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == KEYDOWN:
                if event.key == K_1:
                elif event.key == K_2:
                elif event.key == K_3:
                elif event.key == K_4:
                elif event.key == K_5:
                elif event.key == K_6:



def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

if __name__ == '__main__':
    main()