import random
import sys

from pip._vendor.distlib.compat import raw_input

human_score = 0
computer_score = 0
win_rate_of_RPS = [1/3,1/3,1/3]

# dictionaries for each result's matrix
win_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}
tie_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}
lose_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}

t_win_matrix = [[0,0,0],[0,0,0],[0,0,0]]
t_lose_matrix = [[0,0,0],[0,0,0],[0,0,0]]
t_tie_matrix = [[0,0,0],[0,0,0],[0,0,0]]

def generate_random_choice():
    computer_choice = random.choice(["R", "P", "S"]) # create a random choice
    print("Computer's choice is", computer_choice)
    return computer_choice

def prompt_choice():
    my_choice = raw_input("Enter you choice (R/P/S),"
                          "Or hit ENTER to quit: ").upper()
    if len(my_choice) > 1:
        print ("Error! Only 1 characters allowed!")
        sys.exit()
    if not my_choice:
        print("You quit the game.")
        sys.exit()
    if (my_choice == "R") or (my_choice=="S") or (my_choice=="P"):
        return my_choice
    else:
        print("Must be R/S/P!")
        sys.exit()

def compete_board(user_choice, AI_choice):
    global human_score
    global computer_score
    if(user_choice == "R" and AI_choice == "S"):
        human_score = human_score + 1
        return 'w'
    elif(user_choice == "S" and AI_choice == "P"):
        human_score = human_score + 1
        return 'w'
    elif (user_choice == "P" and AI_choice == "R"):
        human_score = human_score + 1
        return 'w'
    elif(user_choice == AI_choice):
        return 't'
    else:
        computer_score = computer_score + 1
        return 'l'

def update_matrix(previous_choice, current_choice, result):

    if result == "w":
        for key, value in win_matrix.items():
            if ('%s%s' % (previous_choice, current_choice) == key):
                win_matrix['%s%s' % (previous_choice, current_choice)] += 1
    elif result == "t":
        for key, value in tie_matrix.items():
            if ('%s%s' % (previous_choice, current_choice) == key):
                tie_matrix['%s%s' % (previous_choice, current_choice)] += 1
    else:
        for key, value in lose_matrix.items():
            if ('%s%s' % (previous_choice, current_choice) == key):
                lose_matrix['%s%s' % (previous_choice, current_choice)] += 1

    return update_transition_matrix(result)

def update_transition_matrix(result):
    pass


def generate_choice_from_machine_learning():
    global win_rate_of_RPS
    previous_choice = ''

    user_choice = prompt_choice()
    computer_choice = generate_random_choice()
    result = compete_board(user_choice, computer_choice)

    #-------------------------
    previous_choice = user_choice
    user_choice = prompt_choice()
    transMatrix = update_matrix(previous_choice, user_choice, result)


def main():
    while(1):
        user_choice = prompt_choice()
        computer_choice = generate_random_choice()
        compete_board(user_choice, computer_choice)

        print("Human score is", human_score)
        print("Computer score is", computer_score)

main()
