import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"s":1,"w":-1, "g":0}
you = youdict[youstr]

reverseDict = {
    1: "snake" , -1 : "water", 0 : "gun"
}

print(f"you chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if (computer==you):
    print("draw")

else:
    if( computer == -1 and you == 1):
        print("You win!")
    elif( computer == -1 and you == 0):
         print("You Lose!")
    elif( computer == 1 and you == 0):
        print("You win!")
    elif( computer == 1 and you == -1):
        print("You Lose!")
    elif( computer==0 and you == -1):
        print("you win!") 
    elif(computer ==0 and you == 1):
        print("you lose!")    
    else:
        print("something went wrong")


      