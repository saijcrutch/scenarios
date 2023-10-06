import random
import time

def number_n():
    from auxiliary_functions import computerSpeak

    guess = 0
    list = random_list_n()
    random_num = random.choice(list)
    
    computerSpeak("Let's see if you can get this. Can you even count from 1 to 100?", 0.05)

    while guess != random_num:
        num = input("What's your guess? ")
        guess = validate(num)
        
        try:
            guess = int(num)
        except ValueError:
            computerSpeak("That's not even a number! I know you're a human but even you have to be smarter than this.", 0.05)
        else:
            if guess > list[-1]:
                computerSpeak("...")
                time.sleep(0.5)
                computerSpeak("Do you not know how to count? I said to 100 not over 100. Guess this is what I should've \
expected from a human. Guess again.", 0.05) 
            elif guess < list[0]:
                computerSpeak(f"Do you really think {guess} is between 1 and 100? -_- Try again.", 0.05)
            elif guess in list:
                print(guess)
            

    computerSpeak("Took you a while but you finally got it.",0.05)

def validate(userInput):
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
   
def random_list_n():
    list = []

    for i in range(101):
        list.append(i)
    
    list.pop(0)

    return list
