import random
print("Welcome to the RPS game!")
pName = input("Please enter your name: ")
pScore = 0
compScore = 0
choices = ['rock','paper','scissors']
def Game():
    global pName
    global pScore
    global compScore
    NumRounds = int(input("Please enter the number of rounds to be played: "))
    i=0
    while i < NumRounds:
        PlayerChoice = input('Please enter either Paper,Rock, or Scissors: ').strip().lower()
        if PlayerChoice != "rock" and PlayerChoice != "paper" and PlayerChoice != "scissors":
            print("Unrecognized command:", PlayerChoice)
            exit()
        CompChoice = random.choice(choices)
        print("The computer chooses ",CompChoice)
        if PlayerChoice == CompChoice:
            pScore += 0
            compScore += 0
        if PlayerChoice == 'scissors' and CompChoice == 'rock':
            compScore += 1
        elif PlayerChoice == 'scissors' and CompChoice == 'paper':
            pScore += 1
        elif PlayerChoice == 'rock' and CompChoice == 'paper':
            compScore += 1
        elif PlayerChoice == 'rock' and CompChoice == 'scissors':
            pScore += 1
        elif PlayerChoice == 'paper' and CompChoice == 'scissors':
            compScore += 1
        elif PlayerChoice == 'paper' and CompChoice == 'rock':
            pScore += 1
        print(pName,"'s current score:",pScore)
        print("Computer's current score:",compScore)
        i+=1

    if pScore > compScore:
        print("Congratulations",pName,", you won the game !")
    elif pScore < compScore :
        print("Better luck next time!")
    elif pScore == compScore:
        print("It is a tie !")
    exit()
Game()

