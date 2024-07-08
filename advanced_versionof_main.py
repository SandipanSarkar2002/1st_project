# advanced version of rock,paper,scissor game
import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (r for Rock, p for Paper, s for Scissor): ").lower()
        if choice in dict_choices:
            return dict_choices[choice]
        else:
            print("Invalid choice. Please enter 'r' for Rock, 'p' for Paper, or 's' for Scissor.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a Draw!"
    elif (user == 1 and computer == 0) or (user == -1 and computer == 1) or (user == 0 and computer == -1):
        return "You win!"
    else:
        return "You lose!"

dict_choices = {"r": 1, "p": -1, "s": 0}
option = {1: "Rock", -1: "Paper", 0: "Scissor"}

print("This is a Rock, Paper, Scissor game.\nYou have to choose from r, p, s to play.")
user_score, computer_score = 0, 0

while True:
    computer = random.choice([1, 0, -1])
    user = get_user_choice()

    print(f"You chose {option[user]}\nComputer chose {option[computer]}")
    result = determine_winner(user, computer)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    print(f"Scores -> You: {user_score}, Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thank you for playing!")
