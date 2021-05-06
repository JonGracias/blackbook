newlist = (("JON GRACIAS", "RELATIONSHIP", "PHONE", "EMAIL", "|"), ("JON GRACIAS", "RELATIONSHIP",
           "PHONE", "EMAIL", "|"), ("JON GRACIAS", "RELATIONSHIP", "PHONE", "EMAIL", "|"))

def listcontacts():
    for i in range(len(newlist)):
        result("|{:<20s} | {:>8s} | {:^12s} | {:^20s} {:>6s}" .format(
            str(newlist[i][0]), str(newlist[i][1]), str(newlist[i][2]), str(newlist[i][3]), str(newlist[i][4])))
      

def exam(): 
    # add a name
    name = "ENTER A NAME:"
    addname = question(name)
    addname = addname[:20]
    # add a relationship
    try:
        relationship = "RELATIONSHIP"
        addrelationship = question(relationship)
        assert len(addrelationship) <= 10, "ERROR! ONLY 10 CHARACTERS ALLOWED."
        result(str((addname, addrelationship)))
    except AssertionError as msg:
        result(str(msg))
        exam()
def question(message):
    message = message
    val = input("-" * 81 + "\n" + message + "\n" + "-" * 81 + "\n")
    return val


def result(message):
    message = message
    print("-" * 81 + "\n" + message + "\n" + "-" * 81 + "\n")

listcontacts()
