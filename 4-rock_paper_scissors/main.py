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

game_images = [rock, paper, scissors]

print("Welcome to rock paper scissors")

user_action = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

#I used random.randint(0,2) because we are determining the actions
computer_action = random.randint(0, 2)

#for computer action, you can also use random.choice(possible_actions)
possible_actions = ["rock", "paper", "scissors"]

print(f"\nYou chose {user_action}, Computer chose {computer_action}.\n")

#condition for rock, paper, scissors
#rock wins aganist scissors
#scissors wins against paper
#paper wins against rock
#writing the conditionals to determine the winner and loser
if computer_action == user_action:
    print(f"You both selected {user_action}. You draw!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors, you win!")
    else:
        print("Paper covers rock. You lose!")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper! You lose")
elif user_action == "scissors":
    if computer_action == "paper":
        print("scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose!")
