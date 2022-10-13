import random
print("**** Welcome to Rock-Paper-Scissor Game ****")

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

game_images=[rock,paper,scissors]

while True:
    user_input=int(input("Enter your choice:\n 0 : Rock\n 1 : Paper\n 2: Scissors\n"))
    print(f'You chose: \n {game_images[user_input]}')

    print("Now it's computer's turn :")
    computer_input = random.randint(0,2)
    print(f'Computer chose: \n {game_images[computer_input]}')

    if user_input == computer_input:
        print("It's a draw.")
    elif user_input == 1 and computer_input == 0:
        print("You win!")
    elif user_input == 2 and computer_input == 0:
        print("You lose")
    elif user_input == 0 and computer_input == 1:
        print("You lose")
    elif user_input == 2 and computer_input == 1:
        print("You win!")
    elif user_input == 0 and computer_input == 2:
        print("You win!")
    elif user_input == 1 and computer_input == 2:
        print("You lose")
    elif user_input >= 3 or user_input < 0:
        print("Oops! You entered an invalid number")
    ans=input("Do you want to play again? (Y/N) \n").lower()
    if ans == 'n':
        break
print("\nThanks for playing!! ")