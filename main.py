import random

# Number Guessing Game
def guessing_game():
    # Generate a random number between 1 and 50
    number_to_guess = random.randint(1, 50)
    attempts = 5  # Set the number of attempts

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 50. Can you guess it?")
    print(f"You have {attempts} attempts to guess the correct number.\n")

    # Start the guessing loop
    for i in range(attempts):
        try:
            user_guess = int(input(f"Attempt {i + 1}: Enter your guess: "))

            if user_guess == number_to_guess:
                print("Congratulations! You guessed the correct number!\n")
                break
            elif user_guess < number_to_guess:
                print("Too low! Try a higher number.\n")
            else:
                print("Too high! Try a lower number.\n")

        except ValueError:
            print("Please enter a valid number.\n")

    else:
        print(f"Sorry, you've used all {attempts} attempts. The correct number was {number_to_guess}.\n")

# Start the game
guessing_game()
