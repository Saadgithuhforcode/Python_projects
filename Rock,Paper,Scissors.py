import random
choices = ["rock", "paper", "scissors"]

while True:
    user_input= input("Enter rock, paper, scissors or quit to end the game: ").lower()
    if user_input == "quit":
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Invalid choice, please try again.")
        continue
    random_number = random.randint(1, 3)
    computer_choice = choices[random_number]
    print(f"Computer chose: {computer_choice}")
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or (user_input == "paper" and computer_choice == "rock") or (user_input == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:        print("You lose!")