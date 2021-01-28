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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(game_images[choice])
print("Computer chose:")
print(game_images[computer_choice])

if choice >= 3 or choice < 0:
    print("You've typed and invalid number, you lost!")
elif choice == 0 and computer_choice == 2:
    print("You won!")
elif choice == 2 and computer_choice == 0:
    print("You lost!")
elif choice > computer_choice:
    print("You won!")
elif computer_choice > choice:
    print("You lost!")
elif choice == computer_choice:
    print("It's a draw!!")

