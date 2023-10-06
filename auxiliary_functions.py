import time
import random

def computerSpeak(computer, timer):
    for i in computer:
        print(i, end='', flush=True)
        time.sleep(timer)
    time.sleep(0.5)
    print("")    
    time.sleep(0.4)

def computerSpeakAni(computer, timer):
    for i in computer:
        print(i, end='', flush=True)
        time.sleep(timer)
    print(end='\r', flush=True)
    print(" "*len(computer), end='\r', flush=True)
    time.sleep(0.5)

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

    print(old, end='\r', flush=True)
    time.sleep(1)
    print(' '*len(old), end='\r', flush=True)
    print(message, end=' ', flush=True)

    for i in math:
        print(i, end=' ', flush=True)
        time.sleep(0.7)
    
    print(end='\r', flush=True)
    if score > original_score and str(pos_neg) == "-=":
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
        time.sleep(0.1)
    
    time.sleep(1)

def randomType(text):
    # Create a list of unique characters from the input text
    unique_chars = list(set(text))

    # Shuffle the list of unique characters
    random.shuffle(unique_chars)

    # Create a dictionary to store characters in their original positions
    char_positions = {char: [] for char in unique_chars}

    # Populate the dictionary with positions of each character in the input text
    for i, char in enumerate(text):
        char_positions[char].append(i)

    # Initialize the typed_text with spaces
    typed_text = [' ' for _ in text]
    
    for char in unique_chars:
        # Shuffle the positions of the character
        random.shuffle(char_positions[char])

        for position in char_positions[char]:
            typed_text[position] = char
            print("".join(typed_text), end="\r", flush=True)
            time.sleep(0.2)

    print()  # Print a newline after finishing

def comma(words):
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        last_word = words[-1]
        words_except_last = ", ".join(words[:-1])
        return f"{words_except_last}, and {last_word}"
    