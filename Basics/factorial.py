num = int(input("Enter the number to check for factorial: "))
fact=1
if(num ==0  or num ==1):
    print("Factorial is : 1")
else:
    for i in range(1,num+1):
        fact =fact*i
    print("Factorial is :   ",fact)
