import time
import random
import sys

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

def backwardsComputerSpeak(computer, timed):
    com = list(computer)
    com1 = []

    for i in com:
        com1.append(i)

    print(''.join(com1), end="\r", flush=True)
    time.sleep(timed)

    for i in range(len(com1[::-1])): 
        time.sleep(0.03)
        print(' '*len(com1), end="\r", flush=True)
        i = com1.pop()
        print(''.join(com1), end='\r', flush=True)
    
    print(' '*len(com1), end='\r', flush=True)
    time.sleep(2)

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
    
def deleteLine(time1):
    print("This is a test line!", end='', flush=True)
    time.sleep(time1)
    print('\r', end='')
    time.sleep(time1)
    print('\r', "THIS IS A NEW LINE.")
    time.sleep(time1)

def timer(seconds):
    count = [*range(0, seconds+1)]    
    counter = []

    for i in count[::-1]:
        counter.append(i)
        count.pop()  

    for i in range(len(counter)):
        print(i, end='\r', flush=True)
        counter.pop()
        time.sleep(1)

def comSpeakTimer(speak, seconds):
    numbers = range(seconds, 0, -1)

    for i in numbers:
        
        sentence = f"{speak} {str(i)}".ljust(50)
        
        print(sentence, end='\r', flush=True)
        time.sleep(1)

    print(f"{speak} {numbers[-1]-1}", end='\r', flush=True)
    backwardsComputerSpeak(f"{speak} {numbers[-1]-1}", 0.9)

comSpeakTimer("This is a test", 10)