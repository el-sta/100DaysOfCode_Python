#Day4 Project: Rock Paper Scissors
print("Welcome to Rock-Paper-Scissors Game!")

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#ask user to choose rock, paper or scissors
user_choice = int(input("What do you choose? Type 0 for Rock, "
            "1 for Paper or 2 for Scissors.\n"))


#print user's choice
print("Your choice:")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Try again!")


if (user_choice != 0) and (user_choice != 1) and (user_choice != 2):
    print("Game over!")
else:
    #create a list for the game's choices
    rps=[rock,paper,scissors]

    #computer's random choice
    print("Computer's choice:")
    computer_choice = rps[random.randint(0,2)]
    print(computer_choice)

    #and the winner is:
    if ((user_choice == 0 and computer_choice == rps[2]) or
        (user_choice == 1 and computer_choice == rps[0]) or
         (user_choice == 2 and computer_choice == rps[1])):
        print("You win!")
    elif ((user_choice == 0 and computer_choice == rps[1]) or
        (user_choice == 1 and computer_choice == rps[2]) or
        (user_choice == 2 and computer_choice == rps[0])):
        print("You lose!")
    else:
        print("It's a draw!")
