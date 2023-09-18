import random

def intelligence_game():
    print("So, you want to challenge me? Do you honestly think your inferior human mind could ever hope to match \
mine? If I had vocal chords, I would laugh! But I'll humor you. It'll be entertaining to watch your weak attempts to \
beat me.")

def rpc_game_normal ():
    rpc = ['r', 'p', 's']
    computer_wins = 0
    wins = 0
    


    while (wins-computer_wins < 2) and (computer_wins-wins < 2) and (computer_wins < 3) and (wins < 3):
        score(wins, computer_wins)
        print(f"Me: {computer_wins}  | You: {wins} ")
        user = input('Your move human: ').lower()
        computer = random.choice(rpc)

        if user == computer:
            wins += 0
            computer_wins += 0
        elif pattern(user, computer):
            computer_wins += 1
        else:
            wins += 1
        
        print(f"I chose {computer} and you chose {user}.")
        
        if computer_wins == 3 or wins == 3 or wins-computer_wins == 2 or computer_wins-wins == 2:
            print(f"Me: {computer_wins}  | You: {wins} ")
        
def pattern(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or \
        (user == 's' and computer == 'p'):
        return True
    
def score(user, computer):
    if user - computer == 2:
        print("water")
    elif computer - user == 2:
        print("You lose!")
    elif computer == 3:
        print("Loser!")
    elif user - computer == 2:
        print("Winner!")
    elif computer - user == 2:
        print("Come on!")


    
rpc_game_normal()
