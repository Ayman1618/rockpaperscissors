import random

def random_selection(choices):
    return random.choice(choices)  # Randomly select an element from choices

def is_winner(player_selection, computer_selection):
    if player_selection == computer_selection:
        return "It's a draw! Go Again"
    elif (player_selection == "rock" and computer_selection == "scissors") or \
         (player_selection == "paper" and computer_selection == "rock") or \
         (player_selection == "scissors" and computer_selection == "paper"):
        return "Congratulations! You won!"
    else:
        return "Oops! You were defeated by the computer."

choices = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Select your warrior (rock, paper, scissors): ").lower()

    if player_choice not in choices:
        print("Invalid choice. Please choose again.")
        continue  # Go back to the beginning of the loop

    computer_choice = random_selection(choices)
    print(f"Player's choice: {player_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")

    result_message = is_winner(player_choice, computer_choice)
    print(result_message)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing. Exiting the program.")
        break  # Exit the loop and end the program
