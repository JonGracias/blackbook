""" Jonathan Gracias
    Game Scripting
    05/05/2021              
    Excercise Byte What's Next"""

# imports
import pickle
import sys
import os

# define dictionaries. conactsdictionary1 is used to create new contacts and read information on .data
# contactsdictionar2 is used to check if save should be sugessted before quitting
contactsdictionary = {"name": {"relationship": " ", "tel": " ", "email": " "}}
contactsdictionary2 = {"name": {"relationship": " ", "tel": " ", "email": " "}}


# create contacts class contains four attributes: name, relationship, phone and email
class contact:
    def __init__(self, name, relationship="none", tel="none", email="none"):
        contactsdictionary[name] = {
            "relationship": relationship, "tel": tel, "email": email}

# Check if .data file exists


def addressbook(dir):
    global contactsdictionary, contactdictionary2, contact_dir
    contact_dir = dir

    if os.path.exists(contact_dir):
        # if it does exist read from .data
        f = open(contact_dir, "rb")
        contactsdictionary = pickle.load(f)
        x = open(dir, "rb")
        contactdictionary2 = pickle.load(x)
    else:
        # If directory file does not exist - prompt and create
        sq = "NO CONTACTS FILE, WOULD YOU LIKE TO CREATE ONE? | 1:YES | 2:NO |"
        create_contact_data = question(sq)
        if create_contact_data == "1":
            f = open(contact_dir, "wb")
            pickle.dump(contactsdictionary, f)
            f.close()
        elif create_contact_data == "2":
            quit()
        else:
            result("INVALID INPUT")

# for quiting the program


def quit():
    global contactdictionary2, contactdictionary
    # check if save should be suggested
    if contactdictionary2 != contactsdictionary:
        message = "WOULD YOU LIKE TO SAVE CHANGES BEFORE QUITTING? | 1:YES | 2:N0 |"
        answer = question(message)
        if answer == "1":
            result("CHANGES SAVED")
            save()
            sys.exit()
        elif answer == "2":
            result("CHANGES NOT SAVED")
            sys.exit()
    else:
        sys.exit()

# save changes


def save():
    global contactdictionary2, contactdictionary
    # check if there are any changes
    if contactdictionary2 == contactsdictionary:
        result("THERE IS NOTHING TO SAVE!")
    else:
        f = open(contact_dir, "wb")
        pickle.dump(contactsdictionary, f)
        f.close()

# list contacts


def listcontacts():
    for key in (contactsdictionary):
        if key == "name":
            result("|{:<20s} | {:>8s} | {:^12s} | {:^20s} {:>6s}" .format(
                "NAME", "RELATIONSHIP", "PHONE", "EMAIL", "|"))
        else:
            result("|{:<20s} | {:^12s} | {:^12s} | {:<25s} {:<0s}".format(
                key, contactsdictionary[key]["relationship"],
                contactsdictionary[key]["tel"], contactsdictionary[key]["email"], "|"))

# add contact


def addcontact():
    # add a name and check if it is longer than 2 characters and trim if it is over 20
    while True:
        name = "ENTER A NAME"
        addname = question(name)
        addname = addname[:20]
        if len(addname.strip()) >= 2:
            break
        result("ERROR! ENTER TWO OR MORE CHARACTERS.")
    # add a relationship and check if it is less than 10 characters
    while True:
        relationship = "RELATIONSHIP"
        addrelationship = question(relationship)
        if len(addrelationship) <= 10:
            break
        result("ERROR! ONLY 10 CHARACTERS ALLOWED.")
    # add telephone number
    tel = "ENTER A PHONE NUMBER:"
    addtel = question(tel)
    # add email
    email = "ENTER AN EMAIL:"
    addemail = question(email)
    # pass to constructor
    contact(addname, addrelationship, addtel, addemail)

# del contacts


def delcontact():
    name = "ENTER THE NAME OF CONTACT TO DELETE:"
    deleted = question(name)
    if deleted in contactsdictionary:
        del contactsdictionary[deleted]
        result(deleted + " HAS BEEN DELETED")
    else:
        result("CONTACT NAME MUST BE EXACT LETTERS, NOT CASE SENSITIVE")

# search for contacts


def search():
    found = 0
    a = []
    # make sure input is more than 2 characters and trim whitespace - or else all names are returned
    while True:
        person = "NAME OF CONTACT"
        name = question(person)
        if len(name.strip()) >= 2:
            break
        result("ERROR! ENTER TWO OR MORE CHARACTERS.")
    # create array of keys that match the two letters given in same order
    for keys in contactsdictionary:
        if name in keys:
            if keys != "name":
                a.append(keys.upper())
            found += 1
    if found == 0:
        # if none matched result is given
        result("CONTACT DOES NOT EXIST.")
    else:
        # give matching contact given
        result("|{:<20s} | {:>8s} | {:^12s} | {:^20s} {:>6s}".format
               ("NAME", "RELATIONSHIP", "PHONE", "EMAIL", "|"))
        for i in range(found):
            # the array of keys made earlier
            b = str(a[i])
            result(("|{:<20s} | {:^12s} | {:^12s} | {:<25s} {:<0s}".format
                    (b, contactsdictionary[b]["relationship"],
                        contactsdictionary[b]["tel"], contactsdictionary[b]["email"], "|")))

# for simplicity i made this input function that formats how prompts appear on screen. Also it makes
# everything caps, so we don't have to worry about case.


def question(message):
    message = message
    val = input("-" * 81 + "\n" + message + "\n" + "-" * 81 + "\n").upper()
    return val

# this function formats the results of the questions so that is easy to read.


def result(message):
    message = message
    print("-" * 81 + "\n" + message + "\n" + "-" * 81 + "\n")
