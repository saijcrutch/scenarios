import time
import random

def computerSpeak(computer):
    for i in computer:
        print(i, end='', flush=True)
        time.sleep(0.03)
    time.sleep(0.5)
    print("")    
    time.sleep(0.4)

def computerConvo(com1, com2):
    for i in com1:
        print(i, end='', flush=True)
        time.sleep(0.05)

    time.sleep(0.5)
    print("")

    for i in com2:
        print(i, end='', flush=True)
        time.sleep(0.05)
    
    time.sleep(0.5)

def inputToInt(userInput):
    input = userInput
    new_list = []
    num_list = [', '.join(i for i in new_list)]
    one_list = set()
    set1 = set()

    for i in range(-2001, 2001):
        new_list.append(i)

    for i in new_list: 
        num_list.append(i)

    for i in num_list:
        one_list.add(str(i))

    for i in one_list:
        if input == i:
            set1.add(i)

    for i in set1:
        return int(i)