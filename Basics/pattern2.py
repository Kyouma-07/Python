num= int(input("Enter the rows: "))
a = 65

for i in range(0,5):
    for j in range(0,i+1):
        b= chr(a)
        print(b, end = " ")
        a+=1
    print()