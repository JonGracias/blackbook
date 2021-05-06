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
                elif event.key == K_1:
                    addcontact()
                elif event.key == K_2:
                    delcontact()
                elif event.key == K_3:
                    search()
                elif event.key == K_4:
                    save()
                elif event.key == K_5:
                    quit()
                else 
                    
                    
       command = input(
           DASH + "ENTER COMMAND | 0:LIST | 1:ADD | 2:DELETE | 3:SEARCH | 4:SAVE | 5:QUIT" + DASH)
       if command == "list" or command == "0":
           listcontacts()
           continue
       # add person
       if command == "add" or command == "1":
           addcontact()
           continue
       # delete person
       elif command == "delete" or command == "2":
           delcontact()
           continue
       # search
       elif command == "search" or command == "3":
           search()
           continue
       # save
       elif command == "save" or command == "4":
           save()
           continue
       # quit
       elif command == "quit" or command == "5":
           quit()
           break
       else:
           print(DASH + "COMMAND NOT FOUND!" + DASH)
           continue


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
