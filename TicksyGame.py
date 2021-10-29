"""
 Ticksy
 To play the game = $10
 Attempt=3
 3 hidden nos.
 luckyno=676-> $10000
 2nd lucky no =454->$250
 3rd = 666-> - $100
 can't guess the number -> return $5
 If any attempt hit the correct one, game end then and there
"""
print("######################################")
print("Welcome to Malaysian Casino")
wallet = 0
while 1:
    print("----------------------------------")
    print("Your wallet Balance is $", wallet)
    print("----------------------------------")
    print("""Press
1. To recharge your wallet
2. To play ticksy game 
3. To exit the game""")
    resp = int(input("Enter your choice: "))
    if resp == 1:
        wallet = wallet + int(
            input("Enter amount in $ you want to add in your wallet: "))
    elif resp == 2:
        print("Are you sure that you want to spent $10 for this game")
        verify = input("Press Y or N to continue: ")
        if verify == 'Y':
            if wallet >= 10:
                wallet = wallet - 10
                print("Welcome to the Ticksy game")
                print("""Game Rules:
You will be given 3 attempts to guess the numbers.
Once you will guess the number the game will terminate 
and if you can't guess the number right then, $5 will 
be added to your account after completion of the game.""")
                num1 = 676
                num2 = 454
                num3 = 666
                i = 1
                flag = 0
                while i <= 3:
                    print("Turn", i)
                    num = int(input("Guess a number: "))
                    if num == num1:
                        print(
                            "Congrats!! You won $10000. We are adding it to your wallet."
                        )
                        wallet = wallet + 10000
                        break
                    elif num == num2:
                        print(
                            "Congrats!! You won $250. We are adding it to your wallet."
                        )
                        wallet = wallet + 250
                        break
                    elif num == num3:
                        print(
                            "Bad Luck!! You lose $100. We are deducting it to your wallet."
                        )
                        wallet = wallet - 100
                        break
                    else:
                        print("Oops!! You guessed it wrong.")
                        flag = flag + 1
                    i = i + 1
                if flag == 3:
                    print(
                        "Sorry!! you loose this game. We are adding $5 to your wallet"
                    )
                    wallet = wallet + 5
            else:
                print("You are low on your balance, please add $", 10 - wallet,
                      " more to continue")
    elif resp == 3:
        break
    else:
        print("You have selected a wrong option")
