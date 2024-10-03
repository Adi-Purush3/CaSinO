import random

player1 = 0
player2 = 0
player3 = 0
player4 = 0

def start():
    ask = input("How many players (2-4)?  ")
    if ask.isdigit():
        ask = int(ask)
        if 1<ask<5:
            print(f"The Game is commencing with {ask} players")
        else:
            print("The number must be beween 2 - 4")
            start()
    else:
        print("Enter a number between 2 - 4")
        start()
    return ask

players = start()
players= int(players)

def scorer(player_score):
    for i in range(1,players+1):
        print(f"Player {i} begin!!!") 
        ulu = 1
        while ulu==1:
            roll = input("Would you like to roll?  [y/n]")
            def dice():
                a = random.randint(1,6)
                return a
            if roll == "y":
                dice()
                dice = dice()
                print(f"Player {i} rolled: {dice}")
                if dice==1:
                    player1=0
                else:
                    player1+=dice
                print(f"Player {i}'s new score is {player1}")
            elif roll=="n":
                print(f"Player {i+1}'s turn!!")
            else:
                print("Answer must be in [y/n] format")
        

