c7 = [" # "," # "," # "," # "," # "," # ",]
c6 = [" # "," # "," # "," # "," # "," # ",]
c5 = [" # "," # "," # "," # "," # "," # ",]
c4 = [" # "," # "," # "," # "," # "," # ",]
c3 = [" # "," # "," # "," # "," # "," # ",]
c2 = [" # "," # "," # "," # "," # "," # ",]
c1 = [" # "," # "," # "," # "," # "," # ",]
numbers = " 1  2  3  4  5  6  7  "
column = [c1,c2,c3,c4,c5,c6,c7]
num = -1
nom = -1
check1 = -1
check2 = 0
check3 = 1
check4 = 2
check5 = 3
check6 = 0
check7 = 0
check8 = 0
board = ""
win = False
inputs = False
P1placed = False    
P2placed = False
Y = -1
X = -1
placed = False
wincon = False
print("\n\nPlayer 1 counter will be X and Player 2 counter will be 0 \n\n")

for i in range(6):
    num = -1
    for i in range(7):
        num += 1
        board += column[num][nom]
    
    nom -= 1
    print(board)
    board = ""
print("")
print(numbers)

num = -1
nom = -1

while win == False:
    while P1placed == False:
        while inputs == False:
            P1place = input("\nPlayer 1 Which column would you like to place your counter in? ")
            if P1place == "1" or P1place == "2" or P1place == "3" or P1place == "4" or P1place == "5" or P1place == "6" or P1place == "7":           
                inputs = True
            else:
                print("\nPlease input a number from 1 - 7")
        inputs = False  
        P1place = int(P1place) 
        P1place -= 1

        while placed == False:

            Y += 1
            
            if Y == 6:
                print("column",P1place + 1,"is full please choose another column")
                placed = True
                Y = -1

            elif column[P1place][Y] == " # ":
                
                column[P1place][Y] = " X "
                P1placed = True
                placed = True
                Y = -1                       

        placed = False
    placed = False
    inputs = False
    
    for i in range(6):
        num = -1
        for i in range(7):
            num += 1
            board += column[num][nom]
    
        nom -= 1
        print(board)
        board = ""
    print("")
    print(numbers)
    num = -1
    nom = -1

    placed = False
    inputs = False
    P2placed = False
    P1placed = False

    
    for m in range(6):           
        check1 += 1

        if column[check2][check1] == " X " and column[check3][check1] == " X " and column[check4][check1] == " X " and column[check5][check1] == " X ":
            win = True
            P2placed = True
            P1win = True


    check1 = 6              
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1



    for m in range(6):
        check1 -= 1

        if column[check2][check1] == " X " and column[check3][check1] == " X " and column[check4][check1] == " X " and column[check5][check1] == " X ":
            win = True
            P1win = True
            P2placed = True

    check1 = -1
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1

    for m in range(6):
        check1 += 1

        if column[check2][check1] == " X " and column[check3][check1] == " X " and column[check4][check1] == " X " and column[check5][check1] == " X ":
            win = True
            P2placed = True
            P1win = True        

    check1 = 6
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1

    for m in range(6):
        check1 -= 1

        if column[check2][check1] == " X " and column[check3][check1] == " X " and column[check4][check1] == " X " and column[check5][check1] == " X ":
            win = True
            P2placed = True
            P1win = True 

    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2
    check5 = 3
    

    for m in range(7):
        check1 += 1
        if column[check1][check2] == " X " and column[check1][check3] == " X " and column[check1][check4] == " X " and column[check1][check5] == " X ":
            win = True
            P2placed = True
            P1win = True
    
    check1 = 7
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1

    for m in range(7):
        check1 -= 1
        if column[check1][check2] == " X " and column[check1][check3] == " X " and column[check1][check4] == " X " and column[check1][check5] == " X ":
            win = True
            P2placed = True
            P1win = True
 
    check1 = -1
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1

    for m in range(7):
        check1 += 1
        if column[check1][check2] == " X " and column[check1][check3] == " X " and column[check1][check4] == " X " and column[check1][check5] == " X ":
            win = True
            P2placed = True
            P1win = True

    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2
    check5 = 0
    check6 = 1
    check7 = 2
    check8 = 3

    for m in range(4):
        check1 += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if column[check1][check5] == " X " and column[check2][check6] == " X " and column[check3][check7] == " X " and column[check4][check8] == " X ":
            win = True
            P2placed = True
            P1win = True 
   
    check5 += 1
    check6 += 1
    check7 += 1
    check8 += 1
    check1 = 4
    check2 = 5
    check3 = 6
    check4 = 7

    for m in range(4):
        check1 -= 1
        check2 -= 1
        check3 -= 1
        check4 -= 1
        if column[check1][check5] == " X " and column[check2][check6] == " X " and column[check3][check7] == " X " and column[check4][check8] == " X ":
            win = True
            P2placed = True
            P1win = True     

    check5 += 1
    check6 += 1
    check7 += 1
    check8 += 1
    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2

    for m in range(4):
        check1 += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if column[check1][check5] == " X " and column[check2][check6] == " X " and column[check3][check7] == " X " and column[check4][check8] == " X ":
            win = True
            P2placed = True
            P1win = True 

    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2
    check5 = 0
    check6 = 1
    check7 = 2
    check8 = 3

    for m in range(4):
        check1 += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if column[check1][check8] == " X " and column[check2][check7] == " X " and column[check3][check6] == " X " and column[check4][check5] == " X ":
            win = True
            P2placed = True
            P1win = True 
   
    check5 += 1
    check6 += 1
    check7 += 1
    check8 += 1
    check1 = 4
    check2 = 5
    check3 = 6
    check4 = 7

    for m in range(4):
        check1 -= 1
        check2 -= 1
        check3 -= 1
        check4 -= 1
        if column[check1][check8] == " X " and column[check2][check7] == " X " and column[check3][check6] == " X " and column[check4][check5] == " X ":
            win = True
            P2placed = True
            P1win = True     

    check5 += 1
    check6 += 1
    check7 += 1
    check8 += 1
    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2

    for m in range(4):
        check1 += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if column[check1][check8] == " X " and column[check2][check7] == " X " and column[check3][check6] == " X " and column[check4][check5] == " X ":
            win = True
            P2placed = True
            P1win = True 

    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2
    check5 = 3
    check6 = 0
    check7 = 0
    check8 = 0


    while P2placed == False:
        while inputs == False:
            P2place = input("\nPlayer 2 Which column would you like to place your counter in? ")
            if P2place == "1" or P2place == "2" or P2place == "3" or P2place == "4" or P2place == "5" or P2place == "6" or P2place == "7":           
                inputs = True
            else:
                print("\nPlease input a number from 1 - 7")
        inputs = False  
        P2place = int(P2place) 
        P2place -= 1

        while placed == False:
            X += 1

            if X == 6:
                print("column",P2place + 1,"is full please choose another column")
                placed = True
                X = -1

            elif column[P2place][X] == " # ":
                column[P2place][X] = " 0 "
                P2placed = True
                placed = True
                X = -1            

    for i in range(6):
        num = -1
        for i in range(7):
            num += 1
            board += column[num][nom]
    
        nom -= 1
        print(board)
        board = ""
    print("")
    print(numbers)
    num = -1
    nom = -1

    placed = False
    inputs = False
    P2placed = False
    P1placed = False


    for m in range(6):           
        check1 += 1

        if column[check2][check1] == " 0 " and column[check3][check1] == " 0 " and column[check4][check1] == " 0 " and column[check5][check1] == " 0 ":
            win = True
            P1win = True


    check1 = 6              
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1



    for m in range(6):
        check1 -= 1

        if column[check2][check1] == " 0 " and column[check3][check1] == " 0 " and column[check4][check1] == " 0 " and column[check5][check1] == " 0 ":
            win = True
            P2win = True

    check1 = -1
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1

    for m in range(6):
        check1 += 1

        if column[check2][check1] == " 0 " and column[check3][check1] == " 0 " and column[check4][check1] == " 0 " and column[check5][check1] == " 0 ":
            win = True
            P2win = True        

    check1 = 6
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1

    for m in range(6):
        check1 -= 1

        if column[check2][check1] == " 0 " and column[check3][check1] == " 0 " and column[check4][check1] == " 0 " and column[check5][check1] == " 0 ":
            win = True
            P2win = True 

    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2
    check5 = 3
    

    for m in range(7):
        check1 += 1
        if column[check1][check2] == " 0 " and column[check1][check3] == " 0 " and column[check1][check4] == " 0 " and column[check1][check5] == " 0 ":
            win = True
            P2win = True
    
    check1 = 7
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1

    for m in range(7):
        check1 -= 1
        if column[check1][check2] == " 0 " and column[check1][check3] == " 0 " and column[check1][check4] == " 0 " and column[check1][check5] == " 0 ":
            win = True
            P2win = True
 
    check1 = -1
    check2 += 1
    check3 += 1
    check4 += 1
    check5 += 1

    for m in range(7):
        check1 += 1
        if column[check1][check2] == " 0 " and column[check1][check3] == " 0 " and column[check1][check4] == " 0 " and column[check1][check5] == " 0 ":
            win = True
            P2win = True

    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2
    check5 = 0
    check6 = 1
    check7 = 2
    check8 = 3

    for m in range(4):
        check1 += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if column[check1][check5] == " 0 " and column[check2][check6] == " 0 " and column[check3][check7] == " 0 " and column[check4][check8] == " 0 ":
            win = True
            P2win = True 
   
    check5 += 1
    check6 += 1
    check7 += 1
    check8 += 1
    check1 = 4
    check2 = 5
    check3 = 6
    check4 = 7

    for m in range(4):
        check1 -= 1
        check2 -= 1
        check3 -= 1
        check4 -= 1
        if column[check1][check5] == " 0 " and column[check2][check6] == " 0 " and column[check3][check7] == " 0 " and column[check4][check8] == " 0 ":
            win = True
            P2win = True     

    check5 += 1
    check6 += 1
    check7 += 1
    check8 += 1
    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2

    for m in range(4):
        check1 += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if column[check1][check5] == " 0 " and column[check2][check6] == " 0 " and column[check3][check7] == " 0 " and column[check4][check8] == " 0 ":
            win = True
            P2win = True 

    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2
    check5 = 0
    check6 = 1
    check7 = 2
    check8 = 3

    for m in range(4):
        check1 += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if column[check1][check8] == " 0 " and column[check2][check7] == " 0 " and column[check3][check6] == " 0 " and column[check4][check5] == " 0 ":
            win = True
            P2win = True 
   
    check5 += 1
    check6 += 1
    check7 += 1
    check8 += 1
    check1 = 4
    check2 = 5
    check3 = 6
    check4 = 7

    for m in range(4):
        check1 -= 1
        check2 -= 1
        check3 -= 1
        check4 -= 1
        if column[check1][check8] == " 0 " and column[check2][check7] == " 0 " and column[check3][check6] == " 0 " and column[check4][check5] == " 0 ":
            win = True
            P2win = True     

    check5 += 1
    check6 += 1
    check7 += 1
    check8 += 1
    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2

    for m in range(4):
        check1 += 1
        check2 += 1
        check3 += 1
        check4 += 1
        if column[check1][check8] == " 0 " and column[check2][check7] == " 0 " and column[check3][check6] == " 0 " and column[check4][check5] == " 0 ":
            win = True           
            P2win = True

    check1 = -1
    check2 = 0
    check3 = 1
    check4 = 2
    check5 = 3
    check6 = 0
    check7 = 0
    check8 = 0
  
    placed = False
    placed = False
    inputs = False

if P1win == True:
    print("You win Player 1")

elif P2win == True:
    print("You win player 2")
