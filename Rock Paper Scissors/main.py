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
          ________)
       ____________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice= int(input("What do you choose? (1 for Rock; 2 for Paper; 3 for Scissors)= "))

if user_choice >= 4 or user_choice <1:
  print("You Typed An Invalid Number, YOU LOSE😜")
else:
  print(game_images[user_choice-1])

  computer_choice = random.randint(1, 3)
  print("Computer chose:")
  print(game_images[computer_choice-1])

  if user_choice == 1 and computer_choice == 3:
    print("YOU WIN!🏆")
  elif user_choice == 3 and computer_choice == 1:
    print("YOU LOSE😜")
  elif computer_choice > user_choice:
    print("YOU LOSE😜")
  elif user_choice > computer_choice:
    print("YOU WIN!🏆")
  elif computer_choice == user_choice:
    print("It's a Draw!👀")
  else:
    print("You Typed An Invalid Number, YOU LOSE😜")



