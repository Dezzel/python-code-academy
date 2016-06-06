"""In this project i built  the game Rock-Paper-Scissors"""
from random import randint
from time import sleep
options = ["R", "P", "S"]
loss_massage = "You lost!"
win_massage = "You win this one!"
def decide_winner(user_choice, computer_choice):
    print ("You selested: %s" % user_choice)
    print ("Computer selesting...")
    sleep(1)
    print ("Computer selested: %s" %computer_choice)
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print ("It's a tie")
    elif (user_choice_index == 0 and computer_choice_index == 2):
        print (win_massage)
    elif (user_choice_index == 1 and computer_choice_index == 0):
        print (win_massage)
    elif (user_choice_index == 2 and computer_choice_index == 1):
        print (win_massage)
    elif (user_choice_index > 2):
        print ("Invalid number")
        return
    else:
        print (loss_massage)
def play_RPS():
    print ("You play in Rock, Paper, Scissors Game!")
    user_choice = input("Select R for Rock, P for Paper, or S for Scissors: ")
    sleep(1)
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, len(options)-1)]
    decide_winner(user_choice, computer_choice)
play_RPS()
