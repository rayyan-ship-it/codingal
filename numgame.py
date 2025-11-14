import random
playing=True
number=str(random.randint(10,20))
print("there will be a range of number from 0 to 9")
print("and u have to guess one number")
while playing:
    guess=input("enter your guess")
    if guess==number:
        print("you have won the game and the number was",number)
        break
    else:
        print("invalid input") 