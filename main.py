import random
import time
import os
import sys
from auxiliary_functions import *
from words import words
from carnival import carnival
from intelligence import intelligence_game
from adventure import adventure
from number_game import validate, random_list_n

current_directory = os.getcwd()
language = input("(1) English\n(2) 中文\n")

if language == '2':
    chinese_directory = os.path.join(current_directory, 'Languages', '中文')
    sys.path.append(chinese_directory)
    from Languages.中文 import main_zh
    print("")
    main_zh.scenarios_zh()


points = 0
goal = 10

def scenarios():
    games = [carnival, intelligence_game, adventure]

    computerSpeak("Hello, user. I am your computer and I want to play a little game. \
I'll present different scenarios and your goal is to attempt to beat them and get as many points as you can. \
You think you're ready? Let's get started.", 0.03)

    while len(games) > 0:
        player = input("Choose your scenario:\nThe Carnival (1)\nThe Intelligence Game (2)\nThe Adventure (3)\nRandom (4) ")

        if player not in ('1', '2', '3', '4'):
            print("Invalid choice. Please choose a valid option.")
            continue

        if player == '1' and carnival in games:
            print("")
            time.sleep(0.5)
            randomType("Carnival")
            time.sleep(0.5)
            print("---")
            carnival()
            games.remove(carnival)
            player = player.replace("The Carnival (1)", "")
        elif player == '2'and intelligence_game in games:
            print("")
            time.sleep(0.5)
            randomType("Intelligence Game")
            time.sleep(0.5)
            print("---")
            intelligence_game()
            games.remove(intelligence_game)
            player = player.replace("The Intelligence Game (2)", "")
        elif player == '3' and adventure in games:
            print("")
            time.sleep(0.5)
            randomType("The Adventure")
            time.sleep(0.5)
            print("---")
            adventure()
            games.remove(adventure)
            player = player.replace("The Adventure (3)", "")
        elif player == '4' and len(games) > 1:
            if len(games) > 1:
                selection = random.choice(games)
                if selection == carnival:
                    print("")
                    time.sleep(0.5)
                    randomType("Carnival")
                    time.sleep(0.5)
                    print("---")
                    carnival()
                    player = player.replace("The Carn1ival (1)", "")
                elif selection == intelligence_game:
                    print("")
                    time.sleep(0.5)
                    randomType("Intelligence Game")
                    time.sleep(0.5)
                    print("---")
                    intelligence_game()
                    player = player.replace("The Intelligence Game (2)", "")
                elif selection == adventure:
                    print("")
                    time.sleep(0.5)
                    randomType("The Adventure")
                    time.sleep(0.5)
                    print("---")
                    adventure()
                    player = player.replace("The Adventure (3)", "")
                elif len(games) == 1:
                    print("There's only one game left to play.")
                    continue
                games.remove(selection)

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

if language == '1':
    print("")
    scenarios()