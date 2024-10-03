import random

# pre-populated list of players (ideal if lots of guaranteed people)
#players = ["Martin", "Craig", "Sue", "Claire", "Dave", "Alice", 
#           "Sonakshi", "Harry", "Jack", "Rose", "Lexi", "Maria", 
 #          "Thomas", "James", "William", "Ada", "Grace", "Jean", 
  #         "Marissa", "Alan"]


# Intro to tool
print("Welcome to JAG's Team Allocator!\nUsing this tool you will be able to input players and they will be assigned to two separate teams with a captain for each team.")

# INPUT PLAYER NAMES - SIMPLY TYPE NAMES WITH SINGLE SPACE BETWEEN THEM
# The below code is to request the input of players names, if you instead want to pre-populate a list rather than type names each time, 
# make the single line of code below a comment (#) and use the list players code at the top of this code by removing the comments (#). 
players = input("\nSo... Who is playing? - \n").split()

# loop 
while True:

    # shuffle the players listed 
    random.shuffle(players)

    # sort out and print team 1
    team1 = players[:len(players)//2]
    print("\nTEAM 1 \nCaptain:- " + random.choice(team1))
    print("Full Team Line-up:- ")
    for player in team1:
        print(player)

    # sort out and print team 2
    team2 = players[len(players)//2:]
    print("\nTEAM 2 \nCaptain:- " + random.choice(team2))
    print("Full Team Line-up - ")
    for player in team2:
        print(player)
        
    response = input("\nPick teams again? (Type y or n ): ")
    if response == "n":
        print("\nThanks for using this tool, best of luck teams!")
        break

