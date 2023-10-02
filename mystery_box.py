import time
import random
from auxiliary_functions import computerSpeakAni

box_num = random.choice(range(1, 11))
boxVisualLives = {
    0: """
    ________
    |      |
    |      |
    |______|
    """,
    1:  f"""
    ✨ {box_num} ✨
    ________
    |      |
    |      |
    |______|
    """,
    2: """
         /
    ____/
    |      |
    |      |
    |______|
    """,
    3: """
    
    |      |
    |      |
    |______|
    """,
    4: """
    💰💰💰💰
    |💰💰💰|
    |💰💰💰| 
    |______|
    """,
    5: """
    🍔🧆🥘🍲
    |🥗🍝🍚|      
    |🍱🍘🍙|
    |______|
    """,
    6: """
    🪂 🪀 🪁
    |🪆 🪃]|
    |🎎🧸🧮|
    |______|
    """,
}
booth = random.choice(range(1, 11))
something = [key for key in boxVisualLives if key not in [0, 1, 2]]
user = random.choice(something)

def prizes(p1):
    possible_prizes = [key for key in boxVisualLives if key not in [0, 1, 2]]
    prize = random.choice(possible_prizes)

    if p1 == 3:
        print(p1)
        possible_prizes.remove(p1)
        print("You won... nothing!")
        p2 = prize
        if p2 == 4:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[4])
            print("I just won $1,000! I quit!")
            print("Well at least you have a box to live in after blowing all your money on this game.")
        elif p2 == 5:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[5])
            print("Look at all this food! I'll be eating good tonight!")
            print("Hope you like the taste of air.")
        elif p2 == 6:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[6])
            print("I have enough toys but I could probably give them away to some kids.")
            print("I hope you have a good imagination because all you'll be playing with is a box.")
    elif p1 == 4:
        print(boxVisualLives[4])
        possible_prizes.remove(p1)
        print("You won... $1,000!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[3])
            print("I won a box of nothing 😭! Guess I have to keep working here.")
            print("Do you think I could borrow $100 from you?")
        elif p2 == 5:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[5])
            print("It's not $1,000 but at least I'll be eating good for the next week.")
            print("You can buy so much cotton candy with $1,000!")
        elif p2 == 6:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[6])
            print("Do you think I could sell these toys online for $1,000?")
            print("Wanna trade boxes?")
    elif p1 == 5:
        print(boxVisualLives[5])
        possible_prizes.remove(p1)
        print("You won... a week's worth of food!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[3])
            print("I can't eat air!")
            print("I'm so hungry. Can I have a bite?")
        elif p2 == 4:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[4])
            print("Woah! I wasn't expecting to get this much money today!")
            print("You have a week's worth of food but I can buy a month's worth with my money!")
        elif p2 == 6:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[6])
            print("I haven't played with toys in so long.")
            print("You have a week's worth of food. I have a week's worth of entertainment.")
    elif p1 == 6:
        print(boxVisualLives[6])
        possible_prizes.remove(p1)
        print("You won... toys!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[3])
            print("I have a box of nothing!")
            print("Sharing is caring. Why don't you share some of your toys?")
        elif p2 == 4:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[4])
            print("I got $1,000!")
            print("I can buy better toys than whatever you have in that box.")
        elif p2 == 5:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(1)
            print(boxVisualLives[5])
            print("I'm about to save a lot of money on lunch.")
            print("Maybe you can use your toy oven to make some cookies.")

def prizes2(p1):
    possible_prizes = [key for key in boxVisualLives if key not in [0, 1, 2]]
    prize = random.choice(possible_prizes)

    if p1 == 3:
        print(boxVisualLives[3])
        possible_prizes.remove(p1)
        print("I won... nothing!")
        p2 = prize
        if p2 == 4:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("\x1B[3mYou'll be leaving $1,000 richer tonight.\x1B[0m")
        elif p2 == 5:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("\x1B[3mYou won't be eating air.\x1B[0m")
        elif p2 == 6:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[6])
            print("\x1B[3mNot your first choice but it's better than literal nothing.\x1B[0m")
    elif p1 == 4:
        print(boxVisualLives[4])
        possible_prizes.remove(p1)
        print("I won... $1,000!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("\x1B[3mGuess it's time to put in extra shifts at work.\x1B[0m")
        elif p2 == 5:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("\x1B[3mFood is just as valuable as money.\x1B[0m")
        elif p2 == 6:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[6])
            print("\x1B[3mMaybe you can sell these toys for $1,000.\x1B[0m")
    elif p1 == 5:
        print(boxVisualLives[5])
        possible_prizes.remove(p1)
        print("I won... a week's worth of food!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("\x1B[3mWell, at least the box is nice.\x1B[0m")
        elif p2 == 4:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("\x1B[3mIf you go to the right store, you can probably more than a weeks worth of groceries.\x1B[0m")
        elif p2 == 6:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[6])
            print("\x1B[3mMaybe the worker will trade his toys for the food.\x1B[0m")
    elif p1 == 6:
        print(boxVisualLives[6])
        possible_prizes.remove(p1)
        print("I won... toys!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("\x1B[3mHaving the toys would be better than this.\x1B[0m")
        elif p2 == 4:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("\x1B[3mYou can buy way more than toys with $1,000\x1B[0m")
        elif p2 == 5:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("\x1B[3mWhy bake fake cookies when you can have the real deal?\x1B[0m")

print("Try to guess the number of this box.")
print(boxVisualLives[0])

while True:
    try:
        player = int(input("Pick a number between 1-10: "))
        if player not in range(1, 11):
            raise ValueError("You have to choose a number between 1-10.")
        break  # Exit the loop if input is valid
    except ValueError as e:
        print(f"{e} is not a number. You have to choose a number.")

while booth != box_num and player != box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    print(box_num)
    time.sleep(0.5)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    time.sleep(0.5)
    print("It seems neither of us guessed correctly. Let's choose again.")
    booth = random.choice(range(1, 11))
    player = int(input("Pick a number between 1-10: "))

if booth == box_num and player != box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    time.sleep(0.5)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    time.sleep(0.5)
    print(boxVisualLives[1])
    print(f"I chose {box_num}.")
    print("\x1B[3mThe box opens.\x1B[0m")
    print(boxVisualLives[2])
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    time.sleep(0.5)
    prizes2(user)
elif booth != box_num and player == box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    time.sleep(0.5)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    time.sleep(0.5)
    print(boxVisualLives[1])
    print(f"You chose {box_num}.")
    print("\x1B[3mThe box opens.\x1B[0m")
    print(boxVisualLives[2])
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    time.sleep(0.5)
    prizes(user)  # Only call the prizes function if the player wins
elif booth == box_num and player == box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    time.sleep(0.5)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    computerSpeakAni("...", 0.3)
    time.sleep(0.5)
    print("Look's like we both guessed correctly. Let's flip a coin for it.")
    player = input("Heads(h) or Tails?(t) ").lower()
    coin = random.choice(['h', 't'])
    if player == coin:
        print(f"It landed on {player} so you get to look in the box.")
        prizes(user)
    else:
        print(f"It landed on {coin} so I get to look in the box.")
        prizes2(user)


