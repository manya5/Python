import random

# Get user's choice and convert to integer
user_choice = input("What do you want? Type 0 for Rock, 1 for Paper, and 2 for Scissors:\n")
if not user_choice.isdigit():  # Check if input is not a number
    print("You typed an invalid number. You lose!")
else:
    user_choice = int(user_choice)
    # Check for valid range
    if user_choice < 0 or user_choice > 2:
        print("You typed an invalid number. You lose!")
    else:
        # Generate computer's choice
        computer_choice = random.randint(0, 2)
        print(f"Computer chose {computer_choice}")

        # Determine the outcome
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")