import random as rd
while(True):
    options = ["Rock","Paper","Scissor"]
    user_choice = input("Enter your choice among rock,paper,scissor : ")
    comp_choice = rd.choice(options)
    print ("Your choice : ",user_choice)
    print ("comp choice : ",comp_choice)
    if user_choice==comp_choice:
        print("Its Tie")
    elif user_choice=="Rock" and comp_choice=="Scissor":
        print ("You Win")
    elif user_choice=="Paper" and comp_choice=="Rock":
        print ("You Win")
    elif user_choice=="Scissor" and comp_choice=="Paper":
        print ("You Win")
    else:
        print ("Computer Wins")
    print ("Thanks for playing!!")