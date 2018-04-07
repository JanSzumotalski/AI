#Methods
import time
import math
import random
print("Hi! Im JAI.")
#commands
while True:
    command = input("Say something ")
    if command == "Hi" or command == "hi" or command == "Good day" or command == "hello there" or command == "Good morning":
        print("Hi!")
    elif command == "What you can do?":
        print("Im on beta. There's only english language, but there will apear new languages. Same with commands.")
    elif command == "What means JAI?":
        print("You don't need to know")
    elif command == "bye":
        print("Bye")
        time.sleep(3)
        break
    elif command == "What time is it?" or command == "What time is it":
        print("It's muffin time!")
    #Help section
    elif command == "help":
        print('Say "Bye"')
    #End of help section
    else:
        wh = ["Whuh?", "Umm...", "Nevermind", "lul"]
        print(wh[random.randint(0, 3)])

