""" Jonathan Gracias
    Game Scripting
    05/05/2021              
    Excercise Byte What's Next"""

# Imports - I wanted to try making an import module so I made webster a dictionary creator.
import webster
# Welcome screen, was planning to make login with accounts but ran out of time
val = input("-" * 81 + "\n" +
            "WELCOME TO BLACK BOOK. PRESS ENTER TO START" + "\n" + "-" * 81 + "\n")


# The whole scope of this program; list contacts, add, delete, search, save, quit
def main():
    # directory name assignment and sending to webster
    contact_dir = "contact.data"
    webster.addressbook(contact_dir)

    # main loop
    while True: 
        # main menu only numbers can be used
        start = "ENTER COMMAND | 0:LIST | 1:ADD | 2:DELETE | 3:SEARCH | 4:SAVE | 5:QUIT"
        command = webster.question(start)
        if command == "0":
            webster.listcontacts()
            continue
        # add person
        elif command == "1":
            webster.addcontact()
            continue
        # delete person
        elif command == "2":
            webster.delcontact()
            continue
        # search
        elif command == "3":
            webster.search()
            continue
        # save
        elif command == "4":
            webster.save()
            continue
        # quit
        elif command == "5":
            webster.quit()
            break
        else:
            webster.result("COMMAND NOT FOUND! MAKE SURE ONLY NUMBERS ARE USED")
            continue


if __name__ == '__main__':
    main()
