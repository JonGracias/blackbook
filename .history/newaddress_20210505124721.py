# Imports
import os
import pickle
import sys
import addict
import pygame
from pygame.locals import *


# Create dictionaries to store information
contactsdictionary1 = addict.contactsdictionary
contactdictionary2 = addict.contactsdictionary
DASH = "\n" + "-" * 81 + "\n"
contact_dir = "contact.data"


def main():
    pygame.init()
    addressbook()
    menu()
    while True:  # main game loop
        checkSave()
        checkForQuit()
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

def menu():
    print(DASH + "ENTER COMMAND | 0:LIST | 1:ADD | 2:DELETE | 3:SEARCH | 4:SAVE | 5:QUIT" + DASH)

def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


def addressbook():
    # Read from directory file
    global contactsdictionary1
    if os.path.exists(contact_dir):
        f = open(contact_dir, "rb")
        contactsdictionary1 = pickle.load(f)

    # If directory file does not exist - prompt and create
    else:
        create_contact_data = input(
            DASH + "NO CONTACTS FILE, WOULD YOU LIKE TO CREATE ONE? | YES | NO |" + DASH).lower()
        if create_contact_data == "yes":
            f = open(contact_dir, "wb")
            pickle.dump(contactsdictionary1, f)
            f.close()
        elif create_contact_data == "no":
            running = False
        else:
            print(DASH + "INVALID INPUT" + DASH)


def checkSave():
    global contactdictionary2
    x = open(contact_dir, "rb")
    contactdictionary2 = pickle.load(x)


def listcontacts():
    for key in (contactsdictionary1):
        if key == "name":
            print((DASH + "|{:<20s} | {:>8s} | {:^12s} | {:^20s} {:>6s}" .format(
                key.upper(), "RELATIONSHIP", "PHONE", "EMAIL", "|") + DASH))
        else:
            print((DASH + "|{:<20s} | {:^12s} | {:^12s} | {:<25s} {:<0s}".format(
                key.upper(), contactsdictionary1[key]["relationship"].upper(),
                contactsdictionary1[key]["tel"], contactsdictionary1[key]["email"].upper(), "|") + DASH))
            print(DASH)


def addcontact():
    addname = input(DASH + "ENTER A NAME:" + DASH)
    addname = addname[:20]
    try:
        addrelationship = (input(DASH + "RELATIONSHIP" + DASH))
        assert len(addrelationship) <= 10, print(
            DASH + "ERROR! ONLY 10 CHARACTERS ALLOWED." + DASH)
    except:
        addrelationship = ("UNDEFINED")
    addtel = input(DASH + "ENTER A PHONE NUMBER:" + DASH)
    addemail = input(DASH + "ENTER AN EMAIL:" + DASH)
    addict.contact(addname.upper(), addrelationship.upper(),
                   addtel, addemail.upper())


def delcontact():
    name = input(
        DASH + "ENTER THE NAME OF CONTACT TO DELETE:" + DASH).upper()
    if name in contactsdictionary1:
        del contactsdictionary1[name]
    else:
        print(DASH + "CONTACT NAME MUST BE EXACT LETTERS, NOT CASE SENSITIVE" + DASH)


def search():
    found = 0
    name = input(
        DASH + "WHO ARE YOU LOOKING FOR?" + DASH).upper()
    for keys in contactsdictionary1:
        if name in keys:
            print((DASH + "|{:<20s} | {:>8s} | {:^12s} | {:^20s} {:>6s}".format("NAME", "RELATIONSHIP", "PHONE", "EMAIL", "|") + DASH))
            print((DASH + "|{:<20s} | {:^12s} | {:^12s} | {:<25s} {:<0s}" + DASH.format(keys.upper(), contactsdictionary1[keys]["relationship"].upper(),contactsdictionary1[keys]["tel"], contactsdictionary1[keys]["email"].upper(), "|") + DASH))
            found += 1
    if found == 0:
        print(DASH + "CONTACT DOES NOT EXIST." + DASH)


def save():
    if contactdictionary2 == contactsdictionary1:
        print(DASH + "THERE IS NOTHING TO SAVE!" + DASH)
    else:
        f=open(contact_dir, "wb")
        pickle.dump(contactsdictionary1, f)
        f.close()


def quit():
    if contactdictionary2 != contactsdictionary1:
        sq=input(DASH + "WOULD YOU LIKE TO SAVE CHANGES BEFORE QUITTING? | Y | N |" + DASH).lower()
        if save == "y":
            save()
            running=False
            pygame.quit()
            sys.exit()
        elif save == "n":
            running=False
            sys.exit()
    else:
        running = False
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    main()
