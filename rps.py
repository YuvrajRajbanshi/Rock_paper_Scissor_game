import random
# print("Hello world ")


allChoices = ["Rock", "Paper", "Scissors"]
computerScore = 0
playScore = 0

print("Rock Paper Scissor Game")


while True:

    for x in range(1, 6):
        print("1.Rock  2.Paper  3.Scissor")

        userInput = int(input("Enter Your Choice "))
        print(f" This is the {x} Round")
        if userInput == 1:
            print("You Choose the Rock")
            userInput = "Rock"
        elif userInput == 2:
            print("You Choose the Paper")
            userInput = "Paper"
        elif userInput == 3:
            print("You choosed Scissors")
            userInput = "Scissors"
        else:
            print("Inavlid choices")
            break

        computerInput = random.choice(allChoices)
        print(f"Computer choosed {computerInput}")

        # from here the scoring logic

        if userInput == computerInput:
            print("Match is drawn")
            computerScore += 1
            playScore += 1

        elif (userInput == "Paper" and computerInput == "Rock") or (userInput == "Rock" and computerInput == "Scissor") or (userInput == "Scissor" and computerInput == "Paper"):
            print("you won this round")
            playScore += 1

        else:
            print("Computer won this round")
            computerScore += 1

    if playScore > computerScore:
        print(f"you won the match {playScore}")

    elif playScore < computerScore:
        print(f"Computer won the match{computerScore}")
    else:
        print("Match is drawn ")
        print("The mathch is finished")

    user_choices = input("Want to play again? (Yes/Exit)")

    if user_choices == "yes" or user_choices == "YES" or user_choices == "Yes":
        continue
    else:
        break
