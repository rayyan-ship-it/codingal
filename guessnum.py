import random
import time
number=random.randint(1,100)
def intro():
    print('may i ask you for your name?')
    global name
    name=input()
    print(name+"we are going ot play a game.Iam thinking of number between 1 and 100")
    if number%2==0:
        x="even"
    else:
        x="odd"
    print("this is an {}number".format(x))
    time.sleep(.5)
    print("go ahead.guess it")
def pick():
    guessestaken=0
    while guessestaken<6:
        time.sleep(.25)
        enter=input("guess:")
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                guesstaken=guessestaken+1
                if guessestaken<6:
                    if guess<number:
                        print("the guess of the number you have entered is too low")
                    if guess>number:
                        print("the guess of the number you have enter is too high")
                    if guess!=number:
                        time.sleep(.5)
                        print("try again")
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("silly goose that number isnt in the range")
                time.sleep(.25)
                print("please enter a number between 1 and 100")
        except:
            print("i dont think that"+enter+"is a number.sorry")
    if guess==number:
        guessestaken=str(guessestaken)
        print("good job,{} you have guessed my number in{}guesses".format(name,guessestaken))
    if guess!=number:
        print("nope the number i was thinking of "+str(number))
playagain="yes"
while playagain=="yes" or playagain=="y":
    intro()
    pick()
    print("do u want to play again")
    playagain=input()