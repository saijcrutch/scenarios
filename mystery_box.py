import time
import random
from auxiliary_functions import computerSpeakAni

box_num = random.choice(range(1, 11))
booth = random.choice(range(1, 11))

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
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    time.sleep(0.5)
    print("It seems neither of us guessed correctly. Let's choose again.")
    booth = random.choice(range(1, 11))
    player = int(input("Pick a number between 1-10: "))

if booth == box_num and player != box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    time.sleep(0.5)
    print(f"I chose {box_num}.")
elif booth != box_num and player == box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    time.sleep(0.5)
elif booth == box_num and player == box_num:
    print(f"I chose {booth} and you chose {player}. Let's see who guessed correctly.")
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    computerSpeakAni("...", 0.5)
    time.sleep(0.5)