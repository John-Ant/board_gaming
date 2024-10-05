

# intro to tool
print("\nThis application is designed to keep track of scores\n\
The final score will then be displayed at the end.\n\n")


# intention at this stage is to include a step asking what game to play
# can list out supported games and then results can be populated in accordance with game rules

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
        break