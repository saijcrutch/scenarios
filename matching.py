import time
import random
from words import words
from auxiliary_functions import backwardsComputerSpeak
from auxiliary_functions import carnivalTalk

def typeAttack():
    p_points = 0
    c_points = 0
    goal = 10
    
    while p_points < goal and c_points < goal:
        numbers = [i for i in random.choices(range(1, 11), k=3)]
        str_numbers = [str(i) for i in numbers]
        wordList = [i for i in random.choices(words, k=3)]
        options = sorted(wordList+str_numbers, key=lambda x: random.random())

        user = input("Pick a number between 1-10: ")
        player = int(user)
        booth = random.choice(range(1, 11))
        print(booth, end='\r', flush=True)
        time.sleep(1)

        if player == booth:
            print(f"You chose {player} and I chose {booth}. Let's pick again.")
            print(player)
            booth = random.choice(range(1, 11))
            time.sleep(1)
        elif player > booth:
            print(f"You chose {player} and I chose {booth}. You go first.")
            print("You have 5 seconds to memorize this.")
            backwardsComputerSpeak(' '.join(options), 5)
            player = input("Type what you saw: ")
            if player != ' '.join(options):
                print("Sorry, wrong answer. My turn.")
                booth = ' '.join(options)
                if booth == ' '.join(options):
                    c_points += 2
                    carnivalTalk(booth)
                    print(f"I have {c_points} points and you have {p_points} points.")
                elif booth != ''.join(options):
                    p_points += 2
            elif player == ''.join(options):
                p_points += 1
                print(f"You have {p_points} points and I have {c_points} points.")
    
    

    
typeAttack()