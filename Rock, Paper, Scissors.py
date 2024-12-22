import random

choices = ["Rock", "Paper", "Scissors"]


def game():
    print()
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors, First to 3 Wins!")

    while user_score < 3 and computer_score < 3:
        computer = random.choice(choices)
        user = str(input("Enter your Choice: "))
        

        if user not in choices:
            print("Invalid Choice, Choose from Rock-Paper-Scissors!")
            continue

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}\n")

        if user == computer:
            print("Draw!")
            print(f"Your Score --> {user_score} | Computer Score --> {computer_score}\n")
            continue
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Scissors" and computer == "Paper") or \
             (user == "Paper" and computer == "Rock"):
            user_score += 1
            print("You Won this Round!")
        else:
            computer_score += 1
            print("Computer Won this Round!")
        print(f"Your Score --> {user_score} | Computer Score --> {computer_score}\n")

    if user_score == 3:
        print("Congrats!, You Won!")
    else:
        print("Game Over!, Computer Won")

game()

again = str(input("Want to play again?? Yes/No: "))
if again == "Yes":
    game()
elif again == "No":
    print("Thanks for Playing!")
else:
    pass