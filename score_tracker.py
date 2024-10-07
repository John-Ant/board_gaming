import score_config


# intro/explainer text 
print("\n=============================\nThis tool will allow you to track scores over multiple rounds\n\
for a list of set games. It also includes a generic score tracker.\n\n\
To select which game you wish to track, please select from the list below:\n\
\n- Fun Facts \
\n- Generic Scoring")

# request what game/tool wish to use
which_app = input("\nWhich game do you wish to play from the list above? ")

# based on above input, find file from the score_config file and run that games score code. 
if which_app == "Fun Facts":
    print("\n=========================\n")
    score_config.fun_facts()

elif which_app == "Generic Scoring":
    print("\n=========================\n")
    score_config.scoring()