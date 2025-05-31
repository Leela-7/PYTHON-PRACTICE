import random

min=0
max=6
computerScore=0
playerScore=0
inPlay = True
x=0
while x<10:
    test=random.randint(min,max)
    print(test)
    x+=1

def gamePlay():
    global inPlay
    while inPlay:
        player= random.randint(min,max)
        computer= random.randint(min,max)
        print(f"You got {player} vs {computer}")
        if(player == computer):
            print("Tie game")
        elif(player > computer):
            print("player wins")
        elif(player < computer):
            print("computer wins")
        inPlay = False

gamePlay()  # Call the function to start the game
