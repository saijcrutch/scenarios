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
    time.sleep(0.5)

def inputToInt():
    number = input("")
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
        if number == i:
            set1.add(i)

    for i in set1:
         print(int(i))
    
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

def score(message, original_score, score, pos_neg):
    sub = original_score - score
    add = original_score + score
    old = f"{message} {str(original_score)}"
    new_sub = f"{message} {str(sub)}"
    new_add = f"{message} {str(add)}"
    add_sub = f"{str(original_score)} {str(pos_neg)} {str(score)}"
    math = add_sub.split()
    point = str(original_score) + ' ' + pos_neg + ' '
    new_point = str(score) + ' ' + pos_neg + ' '



    time.sleep(0.5)
    print(old, end='\r', flush=True)
    time.sleep(1)
    print(' '*len(old), end='\r', flush=True)
    print(message, end=' ', flush=True)

    for i in math:
        print(i, end=' ', flush=True)
        time.sleep(0.9)
    
    print(end='\r', flush=True)
    if score > original_score and str(pos_neg) == "-":
        print(' '*len(new_sub)+' '*len(new_point), end='\r', flush=True)
        print(new_sub)
    elif original_score > score and str(pos_neg) == "-":
        print(' '*len(new_sub)+' '*len(point), end='\r', flush=True)
        print(new_sub)
    elif str(pos_neg) == "+":
        print(' '*len(new_add)+' '*len(point), end='\r', flush=True)
        print(new_add)
        
    



def carnivalTalk(talk):
    lang = talk.split()

    time.sleep(0.3)

    for i in lang:
        print(i, end=' ', flush=True)
        time.sleep(0.8)
    
    print('')
    time.sleep(1)
   
score("My score:", 5, 10, "-")