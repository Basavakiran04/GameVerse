import random

def number_guessing_game():
    print("=" * 40)
    print(" Welcome to Numbers Game")
    print("=" * 40)
    
    print("\n Choose a Level:")
    print("1. Easy:        1-50    |  10 attempts")
    print("2. Medium:      1-100   |   7 attempts")
    print("3. Difficult:   1-200   |   5 attempts")

    level=input("\n Enter your choice (1/2/3):")

    if level=="1":
        low,high,attempts=1,50,10
        level_name="Easy"
    elif level=="2":
        low,high,attempts=1,100,7
        level_name="Medium"
    elif level=="3":
        low,high,attempts=1,200,5
        level_name="Difficult"
    else:
        low,high,attempts=1,100,7
        level_name="Medium"

    secret_number=random.randint(low,high)
    max_attempts = attempts
    score = 100
    previous_guess=[]

    while attempts > 0:

        try:
            guess=int(input(f" Enter your guess ({low}-{high}):"))
        except ValueError:
            print("please enter a valid number!\n")
            continue

        if guess<low or guess>high:
            print(f"Out of range")
            continue

        if guess in previous_guess:
            print(f"You guessed it previously")
            continue

        previous_guess.append(guess)
        attempts -=1
        score -=10

        if guess==secret_number:
            print(" Your guess was correct!!!!!!!!")
            break

        elif guess < secret_number:
            diff = secret_number - guess
            if diff <= 5:
                print(" Very Hot! Go HIGHER!")
            elif diff <= 15:
                print("  Warm! Go HIGHER!")
            else:
                print("  Cold! Go much HIGHER!")
        else:
            diff = guess - secret_number
            if diff <= 5:
                print("Very Hot! Go LOWER!")
            elif diff <= 15:
                print("Warm! Go LOWER!")
            else:
                print("Cold! Go much LOWER!")

        if attempts==0:
            print(f"Game Over! \n The Number was {secret_number}")

    try:
        play_again = input(" Play again? (yes/no): ").lower()
        if play_again in ["yes", "y"]:
            number_guessing_game()
        else:
            print("Thanks for playing!")
    except KeyboardInterrupt:
        print("\n Game interrupted! Thanks for playing!")

number_guessing_game()