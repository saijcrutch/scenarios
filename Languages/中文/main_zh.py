import random
import time
import os
import sys
from auxiliary_functions import *
from words import words
from carnival import carnival
from intelligence import intelligence_game
from adventure import adventure

points = 0
goal = 10

def scenarios_zh():
    games = [carnival, intelligence_game, adventure]

    computerSpeak("用戶好. I am your computer and I want to play a little game. \
I'll present different scenarios and your goal is to attempt to beat them and get as many points as you can. \
You think you're ready? Let's get started.", 0.05)

    while len(games) > 0:
        player = input("Choose your scenario:\nThe Carnival (1)\nThe Intelligence Game (2)\nThe Adventure (3)\nRandom (4) ")

        if player == '1':
            randomType("Carnival")
            time.sleep(0.5)
            carnival()
            games.remove(carnival)
        elif player == '2':
            randomType("Intelligence Game")
            time.sleep(0.5)
            intelligence_game()
            games.remove(intelligence_game)
        elif player == '3':
            randomType("The Adventure")
            time.sleep(0.5)
            adventure()
            games.remove(adventure)
        elif player == '4':
            if len(games) > 1:
                selection = random.choice(games)
                if selection == games[0]:
                    randomType("Carnival")
                    time.sleep(0.5)
                    carnival()
                    games.remove(carnival)
                elif selection == games[1]:
                    randomType("Intelligence Game")
                    time.sleep(0.5)
                    intelligence_game()
                    games.remove(intelligence_game)
                elif selection == games[2]:
                    randomType("The Adventure")
                    time.sleep(0.5)
                    adventure()
                    games.remove(adventure)

        if len(games) <= 1:
            player = player.replace("Random (4)", "")

    if points == 0:
        print(points)
        computerSpeak("I didn't know it was possible but I am genuinely shocked that you managed to not get any points. \
    I think you need to upgrade your skills.")
        points -= 10
        print(f"Points: {points}")
        computerSpeak("You don't deserve have even a 0 with that pitiful performance.", 0.05)
    elif points in range(1, 6):
        print(points)
        computerSpeak("That's about what I expected from a human. Nothing special.", 0.05)
    elif points in range(6, 10):
        print(points)
        computerSpeak("Slightly more than I expected from you. But don't think that you're better than me.", 0.05)
    else:
        print(points)
        computerSpeakAni("...", 0.5)
        computerSpeak("I can't believe this! You, a human, shouldn't have been able to score that high!")

