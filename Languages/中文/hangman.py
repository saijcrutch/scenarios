import random

def hangman_n():
    from words import words
    from auxiliary_functions import computerSpeak
    import string
    import main

    word = valid_words(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 5

    while len(word_letters) > 0 and lives > 0:
        wordlist = [letter if letter in used_letters else '*' for letter in word]
        print(f"This is your attempt so far: {' '.join(wordlist)} | Lives: {lives}")
        print(f"These are the letters you've used: {' '.join(used_letters)}")
        user = input("What is your attempt? (Press 1 to guess entire word.) ").upper()
        

        if user in alphabet - used_letters:
            used_letters.add(user)
            if user in word_letters:
                word_letters.remove(user)
        elif user in used_letters:
            computerSpeak("Your human memory must be failing you. You already used that letter.", 0.05)
        elif user == '1':
            user = input("Oh so you think you know it? I'd like to see you try! ").upper()
            if user == word:
                computerSpeak(f"I'm speechless! I can't believe you guessed {word}. I guess you are kind of smart.", 0.05)
                main.points += 2
                break
            else:
                computerSpeak(f"I knew you couldnt guess {word}! Guess is was too much for your memory.", 0.05)
                lives -= lives
                break
        elif user not in word_letters and user not in used_letters:
            computerSpeak("Wrong. Try again.", 0.05)
            lives -= 1

        if len(word_letters) == 0 and lives > 0:
            computerSpeak(f"You guessed {word}, surprisingly.", 0.05)
            main.points += 1


def valid_words(x):
    from words import words
    # for normal and easy
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()
