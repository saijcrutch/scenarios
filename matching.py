import time
import random
from words import words
from auxiliary_functions import backwardsComputerSpeak

reps = random.choice(range(3,6))
randWords = random.choices(words, k=reps)
randNums = random.choices(range(1, 101), k=reps)
rand = randNums + randWords
randPick = random.shuffle(rand)

def matching():
    clock = 10
    objects = []
    memory = random.choice(randWords, randNums, randPick)

    print(f"You have {clock} seconds to memorize this:")

matching()