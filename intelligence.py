import random
import time

def intelligence_game():
    from rpc import rpc_game_normal
    from hangman import hangman_n
    from number_game import number_n
    from auxiliary_functions import computerSpeak

    computerSpeak("So, you want to challenge me? Do you honestly think your inferior human mind could ever hope to match \
mine? If I had vocal chords, I would laugh! But I'll humor you. It'll be entertaining to watch your weak attempts at \
beating me.", 0.05)
    computerSpeak("The first challenge is a game of hangman. I'll be surprised if you can manage to guess the word I'm thinking \
of.", 0.05)
    hangman_n()
    print("---")
    computerSpeak("Try not to hurt yourself guessing my number.", 0.05)
    number_n()
    print("---")
    computerSpeak("You for sure can't beat me in a game of rock, paper, scissors.", 0.05)
    rpc_game_normal()
    print("---")
    computerSpeak("No matter what, I will always be better than you.", 0.05)

intelligence_game()