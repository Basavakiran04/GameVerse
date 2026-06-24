# let's play a guess game

print("\n Riddle Time!")

print("\nI have a Face and Hands but not legs\nGuess who am I....")

ans=["clock","watch"]
guess=""

while guess not in ans:
    guess=input("\nEnter your answer:").strip().lower()

    if guess not in ans:
        print("try again")
print("Correct answer")