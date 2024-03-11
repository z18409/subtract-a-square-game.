#File: CS112_A1_T2_Game 3_20231071.py.
#Purpose: two player mathimatical game where we have number of coins which each player should choose a non zero square number to subtract from, the player who subtract the last coin win.
#Author: Zainab Mostafa Mohamad Mahmoud
#ID: 20231071


#Subtract a square game:


import random
#identifying random function to use for assigning random value for coins.

while True: #to loop over the whole game

    square_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
    #a list to choose the move from
    
    print("                             ** Welcome to subtract a square game **")
    style = input("Who choose number of coins:\n a) You\n b) Computer\n :").lower()
    # lower function is used to modify the input if user entered A or B in uppercase.

    

    if style == "a":
        try:
            coins = int(input("please enter number of coins:"))

        except:
            print("Error, enter a right answer")
            continue
        
        if coins in square_list:
            print("Error, please enter non square positive number")
            continue
        #to prevent ending game from the 1st turn.

        if coins <= 0 or coins > 1000:
            print ("Error, Enter an 0 < integer < 1000")
            continue
        # to limit number of coins in a specific positive range.

    if style == "b":
        while True:
            coins = random.randint(10,1000)
            if coins not in square_list:
                break
            else:
                continue
    # to obtain a non-square random number for coins.
        
   
   
    if style != "a" and style != "b":
        print ("Error, please enter a right answer ")
        
        continue

    
    print ("number of coins = ",coins)

    
    
    #first player turn:
    
    
    while True:
        print("*First player*")
        while True:
            try:
                move = int(input("please enter your move:"))
            except:
                print("Error, please enter a right answer")
                continue

            if move not in square_list:
                print("please enter a non zero square number")
                continue
    

            
            if move > coins :
                print("please enter a smaller number")
                continue
            break
        if coins != 0:  
            coins -= move 
            print("\n\ncoins = ",coins)
    


        if coins == 0:
            print("Congratulations, you win!!")
            break
        if coins == 0:
            continue
            

    #second player turn:
        print("*Second player*")
    
        while True:
            try:
                move = int(input("please enter your move:"))
            except:
                print("Error, please enter a right answer")
                continue
            if move not in square_list:
                print("please enter a non zero square number")
                continue

            if move > coins:
                print("please enter a smaller number")
                continue
            break
        if coins != 0:
            coins -= move 
            print("\n\ncoins = ",coins)
    


        if coins == 0:
            print("Congratulations, you win!!")
            break

        if coins == 0:
            continue

        


