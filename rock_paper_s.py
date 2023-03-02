#importing randomization for computer's pick
from random import sample

#adding all options
options = ["scissors", "paper", "rock"]

#saving computer's choice and turning it to a str
computer_play = sample(options, 1)
computer_play = "".join(computer_play)

#adding the player's input
player_play = input("Please enter rock, paper or scissors: ").lower()

#checking if input is correct
while player_play not in options:
    print("Wrong input! You must write ROCK, PAPER OR SCISSORS. Try again!")
#if it isn't, player has to try again
    player_play = input("Please enter rock, paper or scissors: ").lower()

game_dict = {
    "paper":"rock", 
    "rock":"scissors", 
    "scissors":"paper"
    }

#check if tie
if player_play == computer_play:
    print("You used:" + player_play + "." + " Computer used: " + computer_play + ".")
    print("It's a tie!")
#check if W or L
else:
    if game_dict[player_play] == computer_play:
        print("You used:" + player_play + "." + " Computer used: " + computer_play + ".")
        print("You WIN!")
    else:
        print("You used:" + player_play + "." + " Computer used: " + computer_play + ".")
        print("You LOSE!")