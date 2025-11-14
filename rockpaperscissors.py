import random
while True:
    user_action=input("enter the choice(rock,paper,scissor)")
    possible_actions=("rock","paper","scissors")
    computer_action=random.choice(possible_actions)
    print("you choose user_action",user_action,"computer choose",computer_action)
    if user_action==computer_action:
        print("its a tie no one wins")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("rock beats scissors")
        else:
            print("paper covers rock and you loose")
    elif user_action=="scissors":
        if computer_action=="rock":
            print("scissors lose to rock")
        else:
            print("scissor cuts paper")
    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers rock and you win")
        else:
            print("scissors cuts paper and you lose")
    play_again=input("play again yes or no")
    if play_again!="yes":
        break
