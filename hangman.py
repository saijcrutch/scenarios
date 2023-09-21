import random
import string
from words import words
from auxiliary_functions import computerSpeak

def hangman_n():
    word = valid_words(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)

    while len(word_letters) > 0:
        wordlist = [letter if letter in used_letters else '*' for letter in word]
        print(f"This is your attempt so far: {' '.join(wordlist)}")
        print(f"This is what you've guessed: {' '.join(used_letters)}")
        user = input("What is your attempt? (Press 1 to guess entire word.) ").upper()
        

        if user in alphabet - used_letters:
            used_letters.add(user)
            if user in word_letters:
                word_letters.remove(user)
        elif user in used_letters:
            computerSpeak("Your human memory must be failing you. You already used that letter.")
        elif user == '1':
            user = input("Oh so you think you know it? I'd like to see you try! ").upper()
            if user == word:
                computerSpeak(f"I'm speechless! I can't believe you guessed {word}. I guess you are kind of smart.")
                break
            else:
                computerSpeak(f"I knew you couldnt guess {word}! Guess is was too much for your memory.")
                break
        else:
            print(computerSpeak("I know the only way you can win is to cheat but I won't let you get away with that."))


        if len(word_letters) == 0:
            computerSpeak(f"You guessed {word}, surprisingly.")


def valid_words(x):
    # for normal and easy
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

hangman_n()