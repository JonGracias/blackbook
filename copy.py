# Imports
import pickle
import os


# Create dictionaries to store information
contactsdictionary = {"name": {"relationship": " ", "tel": " ", "email": " "}}
savedictionary = {"name": {"relationship": " ", "tel": " ", "email": " "}}
DASH = '-' * 81
NAMENOTFOUND = (DASH + "\nCONTACT DOES NOT EXIST.\n" + DASH)


# create contacts class contains four attributes: name, relationship, phone and email
class contact:
    def __init__(self, name, relationship="none", tel="none", email="none"):
        contactsdictionary[name] = {
            "relationship": relationship, "tel": tel, "email": email}


# Operations - add, search, delete, exit, save,
class operation:
    def listcontacts():
        for key in (contactsdictionary):
            if key == "name":
                print(DASH)
                print(("|{:<20s} | {:>8s} | {:^12s} | {:^20s} {:>6s}".format(
                    key.upper(), "RELATIONSHIP", "PHONE", "EMAIL", "|")))
                print(DASH)
            else:
                print(("|{:<20s} | {:^12s} | {:^12s} | {:<25s} {:<0s}".format(
                    key.upper(), contactsdictionary[key]["relationship"].upper(), 
                    contactsdictionary[key]["tel"], contactsdictionary[key]["email"].upper(), "|")))
                print(DASH)


    def addcontact():
        addname = input(DASH + "\nENTER A NAME:\n" + DASH + "\n")
        addname = addname[:20]
        try:
            addrelationship = (input(DASH + "\nRELATIONSHIP\n" + DASH + "\n"))
            assert len(addrelationship) <= 10, print(
                DASH + "\nERROR! ONLY 10 CHARACTERS ALLOWED.\n" + DASH)
        except:
            addrelationship = ("UNDEFINED")
        addtel = input(DASH + "\nENTER A PHONE NUMBER:\n" + DASH + "\n")
        addemail = input(DASH + "\nENTER AN EMAIL:\n" + DASH + "\n")
        contact(addname.upper(), addrelationship.upper(),
                addtel, addemail.upper())


    def delcontact():
        name = input(
            DASH + "\nENTER THE NAME OF CONTACT TO DELETE:\n" + DASH + "\n").upper()
        if name in contactsdictionary:
            del contactsdictionary[name]
        else:
            print(DASH + "\nCONTACT NAME MUST BE EXACT LETTERS, NOT CASE SENSITIVE\n" + DASH)


    def search():
        found = 0
        name = input(
            DASH + "\nWHO ARE YOU LOOKING FOR?\n" + DASH + "\n").upper()
        for keys in contactsdictionary:
            if name in keys:
                print(DASH)
                print(("|{:<20s} | {:>8s} | {:^12s} | {:^20s} {:>6s}".format(
                    "NAME", "RELATIONSHIP", "PHONE", "EMAIL", "|")))
                print(DASH)
                print(("|{:<20s} | {:^12s} | {:^12s} | {:<25s} {:<0s}".format(
                    keys.upper(), contactsdictionary[keys]["relationship"].upper(), 
                    contactsdictionary[keys]["tel"], contactsdictionary[keys]["email"].upper(), "|")))
                print(DASH)
                found += 1
        if found == 0:
            print(NAMENOTFOUND)


    def save():
        if savedictionary == contactsdictionary:
            print(DASH + "\nTHERE IS NOTHING TO SAVE!\n" + DASH)
        else:
            f = open(AdressBook, "wb")
            pickle.dump(contactsdictionary, f)
            f.close()


    def quit():
        if savedictionary != contactsdictionary:
            save = input(
                DASH + "\nWOULD YOU LIKE TO SAVE? | Y | N |\n" + DASH + "\n").lower()
            if save == "y":
                operation.save()
                running = False
            elif save == "n":
                running = False
            else:
                print(DASH + "\nINVALID INPUT\n" + DASH)
                operation.quit()
        else:
            running = False


# Run program
running = True


# Determine if directory file exists
AdressBook = "addressbook.data"


# Read from directory file
if os.path.exists(AdressBook):
    f = open(AdressBook, "rb")
    contactsdictionary = pickle.load(f)


# If directory file does not exist - prompt and create
else:
    createbook = input(
        DASH + "NO CONTACTS FILE, WOULD YOU LIKE TO CREATE ONE? | YES | NO |\n" + DASH + "\n").lower()
    if createbook == "yes":
        f = open(AdressBook, "wb")
        pickle.dump(contactsdictionary, f)
        f.close()
    elif createbook == "no":
        running = False
    else:
        print(DASH + "\nINVALID INPUT\n" + DASH)


# While loop waiting for instructions
while running:
    x = open(AdressBook, "rb")
    savedictionary = pickle.load(x)
    command = input(
        DASH + "\nENTER COMMAND | 0:LIST | 1:ADD | 2:DELETE | 3:SEARCH | 4:SAVE | 5:QUIT\n" + DASH + "\n")
    if command == "list" or command == "0":
        operation.listcontacts()
        continue
    # add person
    if command == "add" or command == "1":
        operation.addcontact()
        continue
    # delete person
    elif command == "delete" or command == "2":
        operation.delcontact()
        continue
    # search
    elif command == "search" or command == "3":
        operation.search()
        continue
    # save
    elif command == "save" or command == "4":
        operation.save()
        continue
    # test
    elif command == "save" or command == "6":
        operation.test()
        continue
    # quit
    elif command == "quit" or command == "5":
        operation.quit()
        break
    else:
        print(DASH + "\nCOMMAND NOT FOUND!\n" + DASH)
        continue
