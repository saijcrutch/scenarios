import time
import random

def typeAttack():
    from words import words
    import main
    from auxiliary_functions import backwardsComputerSpeak
    from auxiliary_functions import carnivalTalk
    from auxiliary_functions import score

    p_points = 0
    c_points = 0
    goal = 10
    
    while p_points < goal and c_points < goal:
        numbers = [i for i in random.choices(range(1, 11), k=2)]
        str_numbers = [str(i) for i in numbers]
        wordList = [i for i in random.choices(words, k=2)]
        options = sorted(wordList+str_numbers, key=lambda x: random.random())
        joined = ' '.join(options)
        joined2 = ''.join(options)
        joined3 = ' '.join(random.sample(options, k=len(options)))
        option = [joined, joined2, joined3]    
        
        booth = random.choice(range(1, 11))
        
        while True:
            try:
                player = int(input("Pick a number between 1-10: "))
                if player not in range(1, 11):
                    raise ValueError("You have to choose a number between 1-10.")
                break  # Exit the loop if input is valid
            except ValueError as e:
                print(f"{e} is not a number. You have to choose a number.")

        if player not in range(1, 11) or player == 0:
            print("You have to choose between 1-10. Pick again.")

        if player == booth and player in range(1, 11):
            print(f"You chose {player} and I chose {booth}. Let's pick again.")
            time.sleep(0.5)
        elif player > booth and player in range(1, 11):
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
                    print(end='\r', flush=True)
                    print(' '*100, end='\r', flush=True)
                    score("My score:", c_points, 2, "+")
                    time.sleep(0.3)
                    print(f"Your score: {p_points}")
                    c_points += 2
                elif booth != ' '.join(options):
                    carnivalTalk(booth)
                    print('')
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
        elif player < booth and player in range(1, 11):
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
        
    if p_points == goal:
        print(f"Your score: {p_points}")
        print(f"My score: {c_points}")
        print("You beat me!")
        main.points += 1
    elif p_points > goal:
        print(f"Your score: {p_points}")
        print(f"My score: {c_points}")
        print("Woah! You're really good!")
        main.points += 2
    elif c_points == goal:
        print(f"My score: {c_points}")
        print(f"Your score: {p_points}")
        question = input("Sorry, you lose! Play again? (Y/N) ").lower()
        while question != 'n' and question != 'y':
            if question == 'y':
                typeAttack()
            elif question == 'n':
                print("Let me know when you want to play again.")
    elif c_points > goal:
        print(f"My score: {c_points}")
        print(f"Your score: {p_points}")
        print("I'm the master at this game!")
        question2 = input("Want to try again and see if you can do better than me? (Y/N) ").lower()
        while question2 != 'n' and question2 != 'y':
            if question2 == 'y':
                typeAttack()
            elif question2 == 'n':
                print("Let me know when you want to play again.")

    