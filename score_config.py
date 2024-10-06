# this file will contain all the code for various games for the games tracker. 

def scoring():
    while True: 

        rounds_total = int(input("How many rounds do you intend to play?  \nTotal No. of Rounds: "))
        rounds_played = 0
        score = 0

        print("\nFIRST ROUND")

        while rounds_played != rounds_total:
            num_to_add = int(input("\nHow many points to add this round? - "))
            score = score + num_to_add
            rounds_played += 1
            print("\nROUND: " + str(rounds_played) + "\nScore is: " + str(score) + "\nRounds remaining: " + str(int(rounds_total) - int(rounds_played)))

            if rounds_played == rounds_total:
                print("\n==========================\nFINAL SCORE IS: " + str(score) + "\n==========================\n")
                again = input("Do you want to use this tracker again? (y/n)\n")
           
        if again != "y":
            print("\nThank you for using this scoring application")
            break
        else:
            print("\n--------------------------\nNEW GAME\n")
            rounds_played == 0


# Fun Facts 
def fun_facts():
    while True: 

        rounds_total = 8 
        rounds_played = 0
        score = 0

        print("\nWelcome to fun facts!\n\
    SETUP:\n\
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

        while rounds_played != rounds_total:
            num_to_add = int(input("\nHow many points to add this round? - "))
            score = score + num_to_add
            rounds_played += 1
            print("\nROUND: " + str(rounds_played) + "\nScore is: " + str(score) + "\nRounds remaining: " + str(int(rounds_total) - int(rounds_played)))

            if rounds_played == rounds_total:
                print("\n==========================\nFINAL SCORE IS: " + str(score) + "\n==========================\n")
                again = input("Do you want to use this tracker again? (y/n)\n")
           
        if again != "y":
            print("\nThank you for using this scoring application")
            break
        else:
            print("\n--------------------------\nNEW GAME\n")
            rounds_played == 0

