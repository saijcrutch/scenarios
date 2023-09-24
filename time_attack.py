import random
import time
from words import words
import threading

def typeAttack():
    timing = random.choice(range(3, 6))
    numbers = random.choice(range(0, 5))
    lives = 1
    if ' ' not in words or '-' not in words:
            randWords = random.sample(words, timing)
    
    print(numbers)

    while lives > 0:
        print("Try to beat the computer. Type the words before the computer gets a chance to.")
        time.sleep(1)
        print(' '.join(randWords))
        user = input("Type your answer: ")
        computer = threading.Timer()
        if computer != numbers:
            computer = random.choice(range(numbers))
        elif computer == numbers:
             print(''.join(randWords))
             lives -= 1
        if user == ' '.join(randWords):
             print('You win!')
             lives -= 1

def computer(number, seconds):
     rand = random.choice(number)
     



typeAttack()
