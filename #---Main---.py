#---Main.py---
from sps import stone_paper_scissor
from Dice import dice

while True:
    print("1.Stone Paper And Scissors")
    print("2.Dice Game")
    print("3.Exit")
    
    choice=input("Enter Choice:")
    if choice=="1":
        stone_paper_scissor()
    elif choice == "2":
        dice()
    elif choice =="3":
        print("GoodBye!")
        break
    else:
        print("Invalid Choice")
        







