num=int(input("Enter the number to check for prime :    "))
flag =0
if( num ==1):
    print("1 is not prime:  ")
    exit(1)
for i in range(2,num//2):
    if (num%i ==0):
        flag=1
        break
    else:
        continue
if(flag == 0):
    print(f"{num} is prime: ")
else:
    print(f"{num} is not prime")
