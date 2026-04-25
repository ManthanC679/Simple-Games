#---STONE PAPER AND SCISSORS--- 

import random

#Simple Stone,Paper and Scissor Game:

def stone_paper_scissor():
    print ("\nStone Paper Scissors")
    
    choices=["stone","paper","scissors"]
    
    user=input("Enter stone, paper or scissors:").lower()
    if user not in choices:
        print ("Invalid Output")
        return
    
    comp=random.choice(choices)
    
    print ("Choose stone, paper or scissors:",user)
    print ("Computer chose:",comp)
    
    if user==comp:
         print("Its a Tie")
    elif (user == "stone" and comp == "scissors") or (user == "paper" and comp == "stone") or (user == "scissors" and comp == "paper"):
        print("You Wins!")
    else:
        print("Computer Wins!")
        
    
        