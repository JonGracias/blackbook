

def start():
    message = "What is secrete code"
    if question(message) == "happy":
        happy()
    else: 
        result("sad")

def question(message):
    message = message
    val = input("-" * 81 + "\n"+ message +"\n" + "-" * 81 + "\n")
    return val

def result(message):
    message = message
    print("-" * 81 + "\n" + message + "\n" + "-" * 81 + "\n")

def happy():
    result("happy")
    
start()
