a= int(input("Enter the starting point: "))
b=int(input("Enter the ending point: "))


for i in range(a,b+1):
    is_prime =0
    for j in range(2,i//2):
        if(i%j == 0):
            is_prime = 1
            break
        else:
            continue
    if(is_prime==0):
        print(i)
    