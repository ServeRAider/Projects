#MyLuckySeven.py
"""

Purpose: Simulate lucky 7 game and figure out how many tries it takes to lose all of your money and 
        what was max in pot 

Design: 
1. Ask user how much they want to play with 
Repeadetly do this until all money is gone - mypot = 0 
    2. Roll two dice, get their value using random numbers between 1-6
    2a. increment number of rolls by 1
    3. Check to see if I got seven as sum of the rolls
    4. If yes, add $4. Else, -$1 from my pot 
"""
#Get user $$ amount they will wager over the game
import random
MyPot = int(input("How much money do you want to spend playing the game? (integar between 1-100): "))
print(f"My Pot is: ${MyPot:1d}")
Numrolls = 0
MaxPot = MyPot
while True:
    Numrolls += 1
    Dice1 = random.randrange(1,7)
    Dice2 = random.randrange(1,7)   #Two random dice between 1-6

    print(f"The two dice rolls are: {Dice1: 1d} and {Dice2:1d}")
    if (Dice1 + Dice2) == 7:
        MyPot +=4
    else:
        MyPot -=1
    print(f"My pot after roll: ${MyPot:1d}")
    if (MyPot > MaxPot):
        MaxPot= MyPot
    if (MyPot == 0):
        break
print (f"Your number of rolls is: {Numrolls:1d} and your max amount you had was: $ {MaxPot:1d}")

