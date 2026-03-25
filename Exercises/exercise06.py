# =========================
# IMPORTS
# =========================
import random
import sys

# =========================
# RANDOM NUMBER DEMO
# =========================
def show_random_numbers():
    print("\n--- Random Numbers ---")
    for _ in range(5):
        print(random.randint(1, 10))


# =========================
# ASK NAME FUNCTION
# =========================
def ask_name(name):
    names = {
        1: "Kallol",
        2: "Sayan",
        3: "Rohit",
        4: "Deep"
    }
    return f"hi, {names.get(name, 'Guest')}"


def greet_random_person():
    print("\n--- Greeting ---")
    random_name = random.randint(1, 4)
    print(ask_name(random_name))


# =========================
# GUESS THE NUMBER GAME
# =========================
def guess_number_game():
    print("\n--- Guess The Number Game ---")
    secret_number = random.randint(1, 20)
    print("I am thinking of a number between 1 and 20.")

    for guesses_taken in range(1, 7):
        print("Take a guess:")
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed my number in {guesses_taken} guesses!")
            return

    print(f"Nope. The number I was thinking of was {secret_number}")


# =========================
# EXIT HANDLER
# =========================
def exit_program():
    print("\n--- Exit Section ---")
    
    while True:
        print("Type 'exit' to exit:")
        response = input()
        if response.lower() == "exit":
            sys.exit()
        print(f"You typed {response}")

        print("\nAre you want to quit? (yes/no)")
        ans = input().lower()
        if ans == "yes":
            sys.exit()
        else:
            print("You are inside the code.")
            break


# =========================
# MAIN FUNCTION
# =========================
def main():
    show_random_numbers()
    greet_random_person()
    guess_number_game()
    exit_program()


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    main()