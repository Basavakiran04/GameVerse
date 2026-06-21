import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose Rock, Paper, or Scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print(" It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print(" You win!")
    else:
        print(" Computer wins!")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break