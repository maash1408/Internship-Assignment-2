import random

while True:
    number = random.randint(1, 100)
    attempts = 7
    guess_count = 0

    print("Number Guessing Game")
    print("Guess a number between 1 and 100")
    best_score = None

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        guess_count += 1
        attempts -= 1

        if guess == number:
            print("Correct! You guessed it in", guess_count, "attempts")
            break

        elif guess > number:
            print("Too high!")

        else:
            print("Too low!")
        
        if abs(guess - number) <= 5 and guess != number:
            print("Very close!")

        print("Attempts left:", attempts)

    else:
        print("You lost! The number was", number)

    if best_score is None or guess_count < best_score:
        best_score = guess_count
        print("New Best Score!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing")
        break