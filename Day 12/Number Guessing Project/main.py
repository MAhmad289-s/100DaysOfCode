import random

computer_choice = random.randint(1, 100)
easy = 10
hard = 6

def answer_compare(computer_choice, guess, turns):
    if computer_choice == guess:
        print("You guessed right! The computer guessed right!")
        return turns
    elif computer_choice > guess:
        print("you guessed lower!")
        return turns - 1
    elif computer_choice < guess:
        print("you guessed higher!")
        return turns - 1

def difficulty():
    easy_or_hard = input("Choose a difficulty level (easy or hard): ").lower()
    if easy_or_hard == "easy":
        return easy
    else:
        return hard

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns = difficulty()
    guess = None
    while guess != computer_choice and turns > 0:
        print(f"You have {turns} turns left.")
        guess = int(input("Guess a number between 1 and 100: "))
        turns = answer_compare(computer_choice, guess, turns)
        if turns == 0:
            print("Sorry, you lose.")
            print(f"The number was {computer_choice}.")

game()
