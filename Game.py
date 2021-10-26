from random import randint

temp=["rock","paper","scissor"]
comp=temp[randint(0,2)]
count=0
coun=0

while coun!=5 and count!=5:
    player=input("Enter rock,paper,scissor ")
    
    if player==comp:
        print("Tie")
    elif player == "rock":
        
        if comp == "paper":
                print("You lose!", comp, "covers", player)
                coun=coun+1
        else:
                print("You win!", player, "smashes", comp)
                count=count+1
    elif player == "paper":
        if comp == "scissors":
                print("You lose!", comp, "cut", player)
                coun=coun+1
        else:
                print("You win!", player, "covers", comp)
                count=count+1
    elif player == "scissor":
        if comp == "rock":
            print("You lose!", comp, "smashes", player)
            coun=coun+1
        else:
            print("You win!", player, "cut", comp)
            count=count+1
    else:
         print("Not valid")
