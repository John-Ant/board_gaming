import random
import allocate_config



# Intro to tool
print("Welcome to JAG's Team Allocator!\nUsing this tool you will be asked how many teams you want (up to 4 max for now), \nthen you can input players and they will be assigned to the teams with a captain for each team.")

how_many = input("\nHow many teams would you like? (up to 4)  ")

if how_many == "2":
    allocate_config.t2_setup() 

elif how_many == "3":
    allocate_config.t3_setup()

elif how_many == "4":
    allocate_config.t4_setup()