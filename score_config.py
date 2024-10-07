# this file will contain all the code for various games for the games tracker. 


# generic scoring tool for one set of points 
def scoring():
    while True: 

        # introduction to generic scoring application
        print("\nThis application is designed to keep track of one team's scores\n\
You will be asked how many rounds you wish to play.\n\
Scores can then be recorded for each individual round. \n\
The final score will then be displayed at the end.\n\n")
 
        # how many rounds want to play 
        rounds_total = int(input("How many rounds do you intend to play? \n\nTotal No. of Rounds: "))
        rounds_played = 0
        score = 0

        # explains first round
        print("\nFIRST ROUND")

        # loop to add points each round (with exception handling)
        while rounds_played != rounds_total:
            try:
                num_to_add = int(input("\nHow many points to add this round? - "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a number.")
                continue

            # adds score given in round to total tracked score and moves rounds played by +1 
            score += num_to_add
            rounds_played += 1

            # prints out game data each round (round on, current score, rounds remaining)
            print("\nROUND: " + str(rounds_played) + "\nScore is: " + str(score) + "\nRounds remaining: " + str(rounds_total - rounds_played))

            # code to end tracking if rounds played equals round to be played and print results 
            if rounds_played == rounds_total:
                print("\n==========================\nFINAL SCORE IS: " + str(score) + "\n==========================\n")
                again = input("Do you want to use this tracker again? (y/n)\n")
 

        # ask if want to play again with reset feature or application closure. 
        if again != "y":
            print("\nThank you for using this scoring application\n\n")
            quit()
        else:
            print("\n--------------------------\nNEW GAME\n")
            rounds_played == 0




# Fun Facts - scoring for game called Fun Facts 
def fun_facts():
    while True: 
        rounds_total = 8 
        rounds_played = 0
        score = 0

        # game intro 
        print("\nWelcome to the Fun Facts score tracker!\n")

        # how many players (with exception handling)
        players = input("How many people are going to be playing? (Minimum 4 players, Maximum 8 players)  ")
        try:
            players = int(players)
            if players < 4 or players > 8:
                print("ERROR: Please enter a number between 4 and 8.")
                continue
        except ValueError:
            print("ERROR: Invalid input. Please enter a number.")
            continue

        # set up and rules explanation
        print("\n\nSETUP:\n\
        1. Shuffle the cards and place 8 facedown on the table.\n\
        2. Give each player a coloured arrow and the matching marker.\n\
        3. Each player will write their name on one side of the arrow, the other side is blank for now.\n\
        4. Choose a player to take the star, they will be the first player.\n\n\
GAME RULES:\n\
        The first player draws a card and reads the question outloud. \n\
        Then all players secretly answer the question on the blank side of their arrow.\n\
        Once all answers are written, the first player places their arrown on the table facedown.\n\
        Then going clockwise each player places their arrow facedown in relation to the others.\n\
        After all the arrows are placed, the first player can move their own arrow if they feel it will improve the score. \n\
        Now all the arrows are flipped from the lowest to reveal the answers. \n\
        Remove any arrows that were placed incorrectly that break the order from lowest to highest.\n\
        Gain 1 point for each correctly placed arrow.\n\
        Record your scores per round using this score tracking tool.\n\
        Finally move the star to the player on the left and they are the first player for the next round.\n\
        Keep playing until all 8 cards have been used.\n\n\
--------------------------\nFIRST ROUND")

        # loop to add points each round (with exception handling)
        while rounds_played != rounds_total:
            try:
                num_to_add = int(input("\nHow many points to add this round? - "))
            except ValueError:
                print("ERROR: Invalid input. Please enter a number.")
                continue
                
            # adds score given in round to total tracked score and moves rounds played by +1 
            score += num_to_add
            rounds_played += 1
            
            # prints out game data each round (round on, current score, rounds remaining)
            print("\nROUND: " + str(rounds_played) + "\nScore is: " + str(score) + "\nRounds remaining: " + str(rounds_total - rounds_played))


            # code to end tracking if rounds played equals round to be played (in fun facts case 8 rounds) and print results 
            if rounds_played == rounds_total:
                print("\n==========================\nFINAL SCORE IS: " + str(score) + "\n==========================\n")

                # looping if/else if code to grade results as per game rules
                # 4 player scoring 
                if players == 4 and score <= 12:
                    print("Gotta start somewhere. Try again...")
                elif players == 4 and 13 <= score <= 19:
                    print("Totally average, but you could do better.")
                elif players == 4 and 20 <= score <= 26:
                    print("Nice score, you're hitting your stride.")
                elif players == 4 and 27 <= score <= 31:
                    print("Excellent! You're close to perfection.")
                elif players == 4 and score >= 31:
                    print("Perfect! There are no secrets between you - go team!")
                # 5 player scoring
                elif players == 5 and score <= 13:
                    print("Gotta start somewhere. Try again...")
                elif players == 5 and 14 <= score <= 23:
                    print("Totally average, but you could do better.")
                elif players == 5 and 24 <= score <= 33:
                    print("Nice score, you're hitting your stride.")
                elif players == 5 and 34 <= score <= 39:
                    print("Excellent! You're close to perfection.")
                elif players == 5 and score >= 40:
                    print("Perfect! There are no secrets between you - go team!") 
                # 6 player scoring
                elif players == 6 and score <= 15:
                    print("Gotta start somewhere. Try again...")
                elif players == 6 and 16 <= score <= 27:
                    print("Totally average, but you could do better.")
                elif players == 6 and 28 <= score <= 39:
                    print("Nice score, you're hitting your stride.")
                elif players == 6 and 40 <= score <= 47:
                    print("Excellent! You're close to perfection.")
                elif players == 6 and score >= 48:
                    print("Perfect! There are no secrets between you - go team!")
                # 7 player scoring
                elif players == 7 and score <= 17:
                    print("Gotta start somewhere. Try again...")
                elif players == 7 and 18 <= score <= 31:
                    print("Totally average, but you could do better.")
                elif players == 7 and 32 <= score <= 45:
                    print("Nice score, you're hitting your stride.")
                elif players == 7 and 46 <= score <= 55:
                    print("Excellent! You're close to perfection.")
                elif players == 7 and score >= 56:
                    print("Perfect! There are no secrets between you - go team!") 
                # 8 player scoring 
                elif players == 8 and score <= 19:
                    print("Gotta start somewhere. Try again...")
                elif players == 8 and 20 <= score <= 35:
                    print("Totally average, but you could do better.")
                elif players == 8 and 36 <= score <= 51:
                    print("Nice score, you're hitting your stride.")
                elif players == 8 and 52 <= score <= 63:
                    print("Excellent! You're close to perfection.")
                elif players == 8 and score >= 64:
                    print("Perfect! There are no secrets between you - go team!")
                

                # ask if want to play again with reset feature or application closure. 
                again = input("\n---------------------------\n\nDo you want to play again? (y/n)\n")
                if again.lower() != "y":
                    print("\nThank you for using this scoring application\n\n")
                    quit()
                 
                else:
                    rounds_played == 0 
                    print("\n--------------------------\nNEW GAME\n")
                


