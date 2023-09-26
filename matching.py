import time
import random
from words import words
from auxiliary_functions import backwardsComputerSpeak
from auxiliary_functions import carnivalTalk
from auxiliary_functions import score

def typeAttack():
    p_points = 0
    c_points = 0
    goal = 10
    
    while p_points < goal and c_points < goal:
        numbers = [i for i in random.choices(range(1, 11), k=3)]
        str_numbers = [str(i) for i in numbers]
        wordList = [i for i in random.choices(words, k=3)]
        options = sorted(wordList+str_numbers, key=lambda x: random.random())
        joined = ' '.join(options)
        joined2 = ''.join(options)
        joined3 = ' '.join(random.sample(options, k=len(options)))
        option = [joined, joined2, joined3]    
    
        user = input("Pick a number between 1-10: ")
        player = int(user)
        booth = random.choice(range(1, 11))
        print(booth, end='\r', flush=True)
        
        if player == booth and player in list(range(1, 11)):
            print(f"You chose {player} and I chose {booth}. Let's pick again.")
            time.sleep(0.5)
        elif player > booth and player in list(range(1, 11)):
            print(f"You chose {player} and I chose {booth}. You go first.")
            time.sleep(0.5)
            print("You have 5 seconds to memorize this.")
            backwardsComputerSpeak(' '.join(options), 5)
            player = input("Type what you saw: ")
            if player != ' '.join(options):
                print("Sorry, wrong answer. My turn.")
                time.sleep(0.5)
                booth = random.choice(option)
                if booth == ' '.join(options):
                    carnivalTalk(booth)
                    score("My score:", c_points, 2, "+")
                    time.sleep(0.3)
                    print(f"Your score: {p_points}")
                    c_points += 2
                elif booth != ' '.join(options):
                    carnivalTalk(booth)
                    time.sleep(0.5)
                    print("I was wrong. The points go to you.")
                    time.sleep(0.5)
                    score("Your score:", p_points, 2, "+")
                    time.sleep(0.3)
                    print(f"My score: {c_points}")
                    p_points += 2
            elif player == ' '.join(options):
                score("Your score:", p_points, 1, "+")
                time.sleep(0.3)
                print(f"My score: {c_points}")
                p_points += 1
        elif player < booth:
            print(f"I chose {booth} and you chose {player}. I go first.")
            time.sleep(0.5)
            print("This is what needs to memorized.")
            backwardsComputerSpeak(' '.join(options), 5)
            if booth != ' '.join(options):
                booth = random.choice(option)
                carnivalTalk(booth)
                time.sleep(0.5)
                print(end='\r', flush=True)
                backwardsComputerSpeak(booth, 0.8)
                time.sleep(1)
                print("Oh no! I got it wrong! It's your turn now.")
                player = input("Type what you saw: ")
                if player == ' '.join(options):
                    score("Your score:", p_points, 2, "+")
                    time.sleep(0.3)
                    print(f"My score: {c_points}")
                    p_points += 2
                elif player != ' '.join(options):
                    print("You were wrong. The points go to me.")
                    time.sleep(0.5)
                    score("My score:", c_points, 2, "+")
                    time.sleep(0.3)
                    print(f"Your score: {p_points}")
                    c_points += 2
        elif player not in list(range(1, 11)):
            print("You have to choose between 1-10. Pick again.")
        
    if p_points == 10:
        print(f"Your score: {p_points}")
        print(f"My score: {c_points}")
        print("You beat me!")
    elif p_points > 10:
        print(f"Your score: {p_points}")
        print(f"My score: {c_points}")
        print("Woah! You're really good!")
    elif c_points == 10:
        print(f"My score: {c_points}")
        print(f"Your score: {p_points}")
        question = input("Sorry, you lose! Play again? (Y/N) ").lower()
        while question != 'n' and question != 'y':
            if question == 'y':
                typeAttack()
            elif question == 'n':
                print("Let me know when you want to play again.")
    elif c_points > 10:
        print(f"My score: {c_points}")
        print(f"Your score: {p_points}")
        print("I'm the master at this game!")
        question2 = input("SWant to try again and see if you can do better than me? (Y/N) ").lower()
        while question2 != 'n' and question2 != 'y':
            if question2 == 'y':
                typeAttack()
            elif question2 == 'n':
                print("Let me know when you want to play again.")

    
typeAttack()