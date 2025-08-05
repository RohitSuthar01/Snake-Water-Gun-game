import random
"""
1 for the snake
-1 for the water
0 for the gun
"""
computer = random.choice([-1,0,1])
you = input("Enter your Choice :")
youDict = {'s':1,'w':-1,'g':0}
youNum = youDict[you]

#check the condition for the cheaking the user imput and computer input

if(computer == youNum):
    print("it's Draw !")
else:
    if(computer == -1 and youNum == 0):
        print("You Lose !")

    elif(computer == 1 and youNum == 0):
        print("You Win !")

    elif(computer == -1 and youNum == 1):
        print("You Win !")

    elif(computer == 1 and youNum == -1):
        print("You lose !")

    elif(computer == 1 and youNum == 0):
        print("You Win !")

    elif(computer == -1 and youNum == 0):
        print("You lose !")

    elif(computer == 0 and youNum == 1):
        print("You lose !")

    elif(computer == 0 and youNum == -1):
        print("You Win !")

    else:print("Smething went wrong !")
