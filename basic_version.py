import random
import sys

from pip._vendor.distlib.compat import raw_input

human_score = 0
computer_score = 0

def generate_random_choice():
    computer_choice = random.choice(["R", "P", "S"]) # create a random choice
    print("Computer's choice is", computer_choice)
    return computer_choice

def prompt_choice():
    my_choice = raw_input("Enter you choice (R/P/S): ").upper()
    if len(my_choice) > 1:
        print ("Error! Only 1 characters allowed!")
        sys.exit()
    if(my_choice == "R") or (my_choice=="S") or (my_choice=="P"):
        return my_choice
    else:
        print("Must be R/P/S.")
        sys.exit()

def compete_board(user_choice, AI_choice):
    if(user_choice == "R" and AI_choice == "S"):
        return 'w'
    elif(user_choice == "S" and AI_choice == "P"):
        return 'w'
    elif (user_choice == "P" and AI_choice == "R"):
        return 'w'
    elif(user_choice == AI_choice):
        print("Game tie.")
    else:
        return 'l'

while(1):
    user_choice = prompt_choice()
    computer_choice = generate_random_choice()
    score = compete_board(user_choice, computer_choice)
    if(score == "w"):
        human_score = human_score+1
    elif(score == "l"):
        computer_score = computer_score + 1
    else:
        continue

    print("Human score is", human_score)
    print("Computer score is", computer_score)

