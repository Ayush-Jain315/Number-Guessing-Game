import random
n=random.randint(1,100)
count=0
while(True):
    print("You have",(10-count),"Chances left")
    count+=1
    i=int(input("Guess a number : "))
    if i==n:
        print("You guesssed right ,[YOU WON]\n")
        break
    elif i>n:
        print("you guessed a number greater than the right number\n")
    else:
        print("you guessed a number smaller than the right number\n")
    if count == 10:
        print("Game Over")
        break
print("No. of guesses you took",count)