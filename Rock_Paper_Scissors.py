import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

def main():
    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice: ").lower()
    if user_choice not in options:
        print("Wrong")
        return

    computer_choice = get_computer_choice()
    print(f"Choice of the opponent: {computer_choice}")
    winner = get_winner(user_choice, computer_choice)
    if winner == "draw":
        print("\033[33mDraw\033[0m")
    elif winner == "lose":
        print("\033[31mYou are a losser\033[0m")
    else:
        print("\033[32mYou are a winner\033[0m")

if __name__ == "__main__":
    main()

