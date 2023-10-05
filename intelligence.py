import random
import time

def intelligence_game():
    from rpc import rpc_game_normal
    from hangman import hangman_n
    from number_game import number_n
    from auxiliary_functions import computerSpeak

    computerSpeak("So, you want to challenge me? Do you honestly think your inferior human mind could ever hope to match \
mine? If I had vocal chords, I would laugh! But I'll humor you. It'll be entertaining to watch your weak attempts to \
beat me.", 0.05)
    hangman_n()
    number_n()
    rpc_game_normal()

