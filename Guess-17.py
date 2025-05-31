num=10
limit=5
cnt=0
playgame=False
guess=0

while guess !=num:
    print("You have " +str(limit-cnt)+ " left")
    guessfirst=input("Enter a number: ")
    if(guessfirst.isnumeric()):
        guess=int(guessfirst)
    cnt+=1
    if((limit-cnt)==0):
        print("U ran out of guesses it was: "+str(num))
        break
else:
    print("You win")