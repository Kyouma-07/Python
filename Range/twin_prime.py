a= int(input("Enter the starting point: "))
b=int(input("Enter the ending point: "))
list1=[]

for i in range(a,b+1):
    is_prime =0
    for j in range(2,i//2):
        if(i%j == 0):
            is_prime = 1
            break
        else:
            continue
    if(is_prime==0):
        list1.append(i)
 
print("Twin primes are: ")  
for k in range(0,len(list1)-1 ):
    if(list1[k] +2 == list1[k+1] ):
        print(list1[k],list1[k+1])