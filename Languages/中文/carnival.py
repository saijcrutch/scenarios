import time
import random

def carnival():
    from mystery_box import mystery
    from matching import typeAttack
    from auxiliary_functions import carnivalTalk

    carnivalTalk("Welcome to the carnival. We have *2* games here that we're sure you will like. \
Plus, we're the only carnival in town so you don't have much of a choice.")
    carnivalTalk("In this game, you have to try and remember the sequence of letters and numbers \
before me. Let's test how good your memory is!")
    print("")
    typeAttack()
    carnivalTalk("Here's a really special game that I'm sure you'll love. You have to guess the \
number of the box and claim your prize. Who knows, you may win big!")
    print("")
    mystery()