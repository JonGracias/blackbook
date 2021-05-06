# Imports
import os
import pickle
import sys
import pygame
import addict


# Create dictionaries to store information
contactsdictionary1 = addict.contactsdictionary
contactdictionary2 = addict.contactsdictionary
DASH = "\n" + "-" * 81
contact_dir = "contact.data"


def main():
    pygame.init()
    running = True
    addressbook()
    # While loop waiting for instructions
    while running:  # main game loop
        checkSave()
        checkForQuit()
        print(DASH + "ENTER COMMAND | 0:LIST | 1:ADD | 2:DELETE | 3:SEARCH | 4:SAVE | 5:QUIT" + DASH)
        for event in pygame.event.get():  # event handling loop
            if event.type == KEYDOWN:
                if event.key == K_0:
                    listcontacts()
                    continue
                elif event.key == K_1:
                    addcontact()
                    continue
                elif event.key == K_2:
                    delcontact()
                    continue
                elif event.key == K_3:
                    search()
                    continue
                elif event.key == K_4:
                    save()
                    continue
                elif event.key == K_5:
                    quit()
                    break
                    
                    


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
