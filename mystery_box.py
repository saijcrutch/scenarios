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
    🐟🐟🐟🐟
    |🐟🐟🐟|      
    |🐟🐟🐟|
    |______|
    """,
    6: """
    🗑🗑🗑🗑
    |🗑🗑🗑|
    |🗑🗑🗑|
    |______|
    """,
}
booth = random.choice(range(1, 11))
prize = random.choice(boxVisualLives)

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
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    time.sleep(0.5)
    print("It seems neither of us guessed correctly. Let's choose again.")
    booth = random.choice(range(1, 11))
    player = int(input("Pick a number between 1-10: "))

if booth == box_num and player != box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    time.sleep(0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    time.sleep(0.5)
    print(boxVisualLives[1])
    print(f"I chose {box_num}.")
    print("\x1B[3mThe box opens.\x1B[0m")
    print(boxVisualLives[2])
elif booth != box_num and player == box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    time.sleep(0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    time.sleep(0.5)
    print(boxVisualLives[1])
    print(f"You chose {box_num}.")
    print("\x1B[3mThe box opens.\x1B[0m")
    print(boxVisualLives[2])
    time.sleep(0.5)
    print("Do you want to look inside or do you want to give it to the carnival worker?")
    player = input("Look. (Y) Give it away. (N) ").lower()
    if player == 'n':
        print("You give it to the carnival worker.")
        print(prize)
elif booth == box_num and player == box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    time.sleep(0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    time.sleep(0.5)

def prizes(p1, p2, reward):
    nothing = ['0', '1', '2']
    
    for key in boxVisualLives:
        boxVisualLives.pop(nothing)

    p1 = random.choice(boxVisualLives)
    choices = [x for x in boxVisualLives != p1]
    p2 = random.choice(choices)

    if p1 == boxVisualLives[3]:
        p1 = boxVisualLives.pop(p1)
        print("You won... nothing!")
        if p2 == boxVisualLives[4]:
            print("I just won $10,000! I quit!")
            print("Well at least you have a box to live in after blowing all your money on this game.")
        elif p2 == boxVisualLives[5]:
            print("Idk")
        elif p2 == boxVisualLives[6]:
            print("Idk what to do.")
    