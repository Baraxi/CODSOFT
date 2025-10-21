import random

def get_user_choice():
    while True:
        choice = input("Choose Rock(1), Paper(2), or Scissors(3): ").lower()
        if choice in ['1', 'rock']:
            return 1
        elif choice in ['2', 'paper']:
            return 2
        elif choice in ['3', 'scissors']:
            return 3
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    win_conditions = {
        1: 3,  # Rock beats Scissors
        2: 1,  # Paper beats Rock
        3: 2   # Scissors beats Paper
    }
    return "You win!" if win_conditions[user_choice] == computer_choice else "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        print(f"You chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        if input("Play again? (yes/no): ").lower() != 'yes':
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You won!")
            elif user_score < computer_score:
                print("Computer wins!")
            else:
                print("It's a tie!")
            print("Thanks for playing!")
            break

play_game()