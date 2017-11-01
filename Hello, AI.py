import time
import math
import random
print("Hi! Im JAI.")
while True:
    command = input()
    if command == "Hi":
        print("Hi!")
    elif command == "What you can do?":
        print("Im on beta. There's only english language, but there will apear new languages. Same with commands.")
    elif command == "What means JAI?":
        print('That means "Jan Artificial Intelligence"')
    elif command == "Bye":
        print("Bye. I will forgot everything, but maybe in near feature.")
        break
    elif command == "What time is it?":
        print("It's muffin time!")
        
    else:
        wh = ["What?", "Huh?"]
        print(wh[random.randint(0, 1)])

