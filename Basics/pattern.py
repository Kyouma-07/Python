num = int(input("Enter the the number of rows to be printed :   "))
a= 65
for i in range(0,5):
    for j in range(a,a+i+1):
        print(chr(j),end = " ")
    print()