import random

def t2_setup(): 
  
  while True:

    players = input("\nSo... Who is playing? - \n").split()
    # shuffle the players listed 
    random.shuffle(players)

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


def t3_setup():
  
  while True:

    players = input("\nSo... Who is playing? - \n").split()
    # shuffle the players listed 
    random.shuffle(players)

    # sort out team 1
    team1 = players[:len(players)//3]
    print("\nTEAM 1 \nCaptain:- " + random.choice(team1))
    print("Full Team Line-up:- ")
    for player in team1:
        print(player)

    # sort out team 2
    team2 = players[len(players)//3:(len(players)//3)*2]
    print("\nTEAM 2 \nCaptain:- " + random.choice(team2))
    print("Full Team Line-up:- ")
    for player in team2:
        print(player)

    # sort out and print team 3
    team3 = players[(len(players)//3)*2:]
    print("\nTEAM 3 \nCaptain:- " + random.choice(team3))
    print("Full Team Line-up - ")
    for player in team3:
        print(player)
        
    response = input("\nPick teams again? (Type y or n ): ")
    if response == "n":
        print("\nThanks for using this tool, best of luck teams!")
        break


def t4_setup():
  
  while True:

    players = input("\nSo... Who is playing? - \n").split()
    # shuffle the players listed 
    random.shuffle(players)

    team_size = len(players)//4

    # sort out team 1
    team1 = players[:team_size]
    print("\nTEAM 1 \nCaptain:- " + random.choice(team1))
    print("Full Team Line-up:- ")
    for player in team1:
        print(player)

    # sort out team 2
    team2 = players[team_size:team_size*2]
    print("\nTEAM 2 \nCaptain:- " + random.choice(team2))
    print("Full Team Line-up:- ")
    for player in team2:
        print(player)

    # sort out and print team 3
    team3 = players[team_size*2:team_size*3]
    print("\nTEAM 3 \nCaptain:- " + random.choice(team3))
    print("Full Team Line-up - ")
    for player in team3:
        print(player)

    # sort out and print team 4
    team4 = players[team_size*3:]
    print("\nTEAM 4 \nCaptain:- " + random.choice(team4))
    print("Full Team Line-up - ")
    for player in team4:
        print(player)

       

    response = input("\nPick teams again? (Type y or n ): ")
    if response == "n":
        print("\nThanks for using this tool, best of luck teams!")
        break