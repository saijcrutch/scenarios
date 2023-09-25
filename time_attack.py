import random
import time
from words import words
import threading

def typeAttack():
    timing = random.choice(range(3, 6))
    numbers = random.choice(range(3, 6))
    lives = 1
    if ' ' not in words or '-' not in words:
            randWords = random.sample(words, timing)
    
    print(numbers)

    while lives > 0:
        print("Try to beat the computer. Type the words before the computer gets a chance to.")
        time.sleep(1)
        rand = ' '.join(randWords)
        print(rand)
        com = threading.Timer(5.0, computer, [rand])
        com.start()
        user = input("Type your answer: ")
        if com != numbers:
            print("ugh")
        elif com == rand:
             com = rand
             print(com)
             print("You lose!")
             lives -= 1
             break
        elif user == rand:
             print('You win!')
             lives -= 1
             break

def computer(*number):
      print(''.join(number))
     
     
     



typeAttack()
