import random

computer = random.choice([-1, 0, 1])
player = input("Enter your choice : ")
youDict = {"s" : 1, "w" : 0, "g" : -1}
reverseDict = {1 : "s", 0 : "w", -1 : "g"}

you  = youDict[player]

print(f"Computer chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(you == computer):
    print("It's a tie" )

else:
    if (computer == -1 and you == 1):
        print("You win")
    elif (computer == 1 and you == -1):
        print("Computer wins")      
    elif (you > computer):
        print("You win")
    else:        print("Computer wins")