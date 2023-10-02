from mystery_box import boxVisualLives
import time
import random

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
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("I just won $1,000! I quit!")
            print("Well at least you have a box to live in after blowing all your money on this game.")
        elif p2 == 5:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("Look at all this food! I'll be eating good tonight!")
            print("Hope you like the taste of air.")
        elif p2 == 6:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(0.5)
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
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("I won a box of nothing 😭! Guess I have to keep working here.")
            print("Do you think I could borrow $100 from you?")
        elif p2 == 5:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("It's not $1,000 but at least I'll be eating good for the next week.")
            print("You can buy so much cotton candy with $1,000!")
        elif p2 == 6:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(0.5)
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
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("I can't eat air!")
            print("I'm so hungry. Can I have a bite?")
        elif p2 == 4:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("Woah! I wasn't expecting to get this much money today!")
            print("You have a week's worth of food but I can buy a month's worth with my money!")
        elif p2 == 6:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(0.5)
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
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("I have a box of nothing!")
            print("Sharing is caring. Why don't you share some of your toys?")
        elif p2 == 4:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("I got $1,000!")
            print("I can buy better toys than whatever you have in that box.")
        elif p2 == 5:
            print("\x1B[3mThe carnival worker chooses another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("I'm about to save a lot of money on lunch.")
            print("Maybe you can use your toy oven to make some cookies.")

def prizes2(p1):
    possible_prizes = [key for key in boxVisualLives if key not in [0, 1, 2]]
    prize = random.choice(possible_prizes)

    if p1 == 3:
        print(p1)
        possible_prizes.remove(p1)
        print("I won... nothing!")
        p2 = prize
        if p2 == 4:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("I just won $1,000! I quit!")
            print("Well at least you have a box to live in after blowing all your money on this game.")
        elif p2 == 5:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("Look at all this food! I'll be eating good tonight!")
            print("Hope you like the taste of air.")
        elif p2 == 6:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[6])
            print("I have enough toys but I could probably give them away to some kids.")
            print("I hope you have a good imagination because all you'll be playing with is a box.")
    elif p1 == 4:
        print(boxVisualLives[4])
        possible_prizes.remove(p1)
        print("You won... $1,000!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("I won a box of nothing 😭! Guess I have to keep working here.")
            print("Do you think I could borrow $100 from you?")
        elif p2 == 5:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("It's not $1,000 but at least I'll be eating good for the next week.")
            print("You can buy so much cotton candy with $1,000!")
        elif p2 == 6:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[6])
            print("Do you think I could sell these toys online for $1,000?")
            print("Wanna trade boxes?")
    elif p1 == 5:
        print(boxVisualLives[5])
        possible_prizes.remove(p1)
        print("You won... a week's worth of food!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("I can't eat air!")
            print("I'm so hungry. Can I have a bite?")
        elif p2 == 4:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("Woah! I wasn't expecting to get this much money today!")
            print("You have a week's worth of food but I can buy a month's worth with my money!")
        elif p2 == 6:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[6])
            print("I haven't played with toys in so long.")
            print("You have a week's worth of food. I have a week's worth of entertainment.")
    elif p1 == 6:
        print(boxVisualLives[6])
        possible_prizes.remove(p1)
        print("You won... toys!")
        p2 = prize
        if p2 == 3:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[3])
            print("I have a box of nothing!")
            print("Sharing is caring. Why don't you share some of your toys?")
        elif p2 == 4:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[4])
            print("I got $1,000!")
            print("I can buy better toys than whatever you have in that box.")
        elif p2 == 5:
            print("\x1B[3mYou choose another box at random.\x1B[0m")
            time.sleep(0.5)
            print(boxVisualLives[5])
            print("I'm about to save a lot of money on lunch.")
            print("Maybe you can use your toy oven to make some cookies.")