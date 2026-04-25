
import random
def dice():
    print("\nDice Game")
    
    input("Press Enter To Roll")
    
    user=random.randint(1,6)
    comp=random.randint(1,6)
    
    print ("You Got:",user)
    print ("Computer Got:",comp)
    
    if user > comp: 
        print("Result:You win") 
    elif user < comp: 
        print("Result:Computer wins")
    else: 
        print("Result:Tie")
        
    
        
    
        
    