'''
rock,paper,scissor game
rock=1
paper=-1
scissor=0
'''
import random

print("This is a Rock,Paper,Scissor game.\n You have to choose from r,p,s to play.")

computer = random.choice([1,0,-1])
choice=input("Enter your choice : ")
dict={"r":1,"p":-1,"s":0}
if choice not in dict:
    print("Invalid choice. Please enter 'r' for Rock, 'p' for Paper, or 's' for Scissor.")
else:
    you=dict[choice]
    option={1:"Rock",-1:"Paper",0:"Scissor"}

    print(f"You chose {option[you]}\n Computer chose {option[computer]}")

    if(computer == you):
        print("It's a Draw !")
    else:
        if(computer == 1 and you==0):
            print("You lose !")
        elif(computer == -1 and you==0):
            print("You win !")
        elif(computer == 1 and you== -1):
            print("You win !")
        elif(computer == -1 and you== 1):
            print("You lose !")
        elif(computer == 0 and you== 1):
            print("You win !")
        elif(computer == 0 and you== -1):
            print("You lose !")
        else:
            print("Something went wrong.")