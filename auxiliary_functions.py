import time
import random

def computerSpeak(computer):
    for i in computer:
        print(i, end='', flush=True)
        time.sleep(0.03)
    time.sleep(0.1)
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
