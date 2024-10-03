import random

# list of players 
players = ["Martin", "Craig", "Sue", "Claire", "Dave", "Alice", 
           "Sonakshi", "Harry", "Jack", "Rose", "Lexi", "Maria", 
           "Thomas", "James", "William", "Ada", "Grace", "Jean", 
           "Marissa", "Alan"]

# Intro to tool
print("Welcome to JAG's Team Allocator!")

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

