import random
import time

def rpc_game_normal ():
    from auxiliary_functions import computerSpeak
    import main

    rpc = ['r', 'p', 's']
    computer_wins = 0
    wins = 0
    
    while (wins-computer_wins < 2) and (computer_wins-wins < 2) and (computer_wins < 3) and (wins < 3):
        print(f"Me: {computer_wins}  | You: {wins} ")
        user = input('Your move human: ').lower()
        computer = random.choice(rpc)

        if user == 'r':
            user = 'rock'
        elif user == 's':
            user = 'scissors'
        elif user == 'p':
            user = 'paper'

        if computer == 'r':
            computer = 'rock'
        elif computer == 's':
            computer = 'scissors'
        elif computer == 'p':
            computer = 'paper'

        computerSpeak(f"You chose {user} and I chose {computer}.")

        if user == computer:
            wins += 0
            computer_wins += 0
        elif pattern(user, computer):
            wins += 1
        elif com_pattern(user, computer):
            computer_wins += 1
        else:
            computerSpeak("Your human tricks won't work on me. Choose a valid character.")
        
        
        
        if computer_wins == 3 or wins == 3 or wins-computer_wins == 2 or computer_wins-wins == 2:
            print(f"Me: {computer_wins}  | You: {wins} ")
        score_n(wins, computer_wins)
        
def pattern(user, computer):
    if (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or \
        (user == 'scissors' and computer == 'paper'):
        return True
    
def com_pattern(user, computer):
    if (computer == 'rock' and user == 'scissors') or (computer == 'paper' and user == 'rock') or \
        (computer == 'scissors' and user == 'paper'):
        return True
    
def score_n(user, computer):
    from auxiliary_functions import computerSpeak
    import main

    if user - computer == 2:
        computerSpeak("You must be sooo proud of yourself, right now.")
        main.points += 1
    elif computer - user == 2:
        computerSpeak("What else were you expecting?")
    elif computer == 3:
        computerSpeak("Loser!")
    elif user == 3:
        computerSpeak("Hmm... I guess you won this time. Surprising.")
        main.points += 2

