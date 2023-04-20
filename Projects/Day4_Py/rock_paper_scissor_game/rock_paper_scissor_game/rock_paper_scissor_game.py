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
import random
users_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computer_pick = random.randint(0,2)
players_pick = int(users_choice)

print(computer_pick)
print(players_pick) 

if players_pick == 0 and computer_pick == 0:
    print("Its a tie")
elif players_pick == 0 and computer_pick == 1:
    print(paper)
    print("You Lose")
elif players_pick == 0 and computer_pick == 2:
    print(rock)
    print("You win")
elif players_pick == 1 and computer_pick == 0:
    print(paper)
    print("You win")
elif players_pick == 1 and computer_pick == 1:
    print("Its a tie")
elif players_pick == 1 and computer_pick == 2:
    print(scissors)
    print("You Lose")
elif players_pick == 2 and computer_pick == 0:
    print("You lose")
elif players_pick == 2 and computer_pick == 1:
    print("You Lose")
elif players_pick == 2 and computer_pick == 2:
    print("Its a tie")
else:
    print("Please pick 0, 1, 2 to play the game")





