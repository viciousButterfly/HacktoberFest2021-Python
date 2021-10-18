import random
def unique_values(given_list):
    unique_list=[]
    for value in given_list:
        if value in unique_list:
            continue
        else:
            unique_list.append(value)
    return unique_list
def display_hand(tries):
    stages = ["""
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / \\
    |
    """,
              """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / 
    | 

            """
        ,
              """
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |      
    | 

            """
        ,
              """
    --------
    |      |
    |      O
    |     \\|
    |      |
    |     
    | 

            """
        ,
              """
    --------
    |      |
    |      O
    |      |
    |      |
    |     
    | 

            """
        ,
              """
    --------
    |      |
    |      O
    |     
    |     
    |     
    | 

            """
        ,
              """
    --------
    |      |
    |     
    |     
    |     
    |     
    | 

            """

              ]
    return stages[tries]
fruit=['apple','banana','strawberry','kiwi','watermelon','peach','orange','berry',
       'blueberry','sapodilla','avacado','cherry','guava','grapes','mango']
word=random.choice(fruit)
chance=6
guess=[]
show=[]
active=False
while not active:
    print(display_hand(chance))
    for letter in word:
        if letter.lower() in guess:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print('\n')
    g=input("attempts left: {} , next guess: ".format(chance))
    show.append(g)
    print(f'Letter Guessed : {unique_values(show)}')

    if g.isalpha()==False:
        print("Enter String only")
        continue
    guess.append(g.lower())
    if g.lower() not in word.lower():
        chance-=1
        if chance==0:
            print(display_hand(0))
            break
    active = True
    for letter in word:
        if letter.lower() not in guess:
            active=False
print('\n')
if active:
    print(f"You found it, the word is : {word.upper()}")
else:
    print(f"Game over ,the word was : {word.upper()}")