#Arithmetic opertors
a= float(input("Enter the first nummber: \n"))
b= float(input("Enter the second nummber:\n"))
print()
print("The sum is:  ", a+b)
print("The difference is:   ", a-b)
print("The product is:  ", a*b)
print("The quotient is: ", a//b)
print("The remainder is: ", a%b)

#relational opertors
if(a==b):
    print(f"{a} is equal to {b}\n")
    
elif(a>b):
    print(f"{a} is greater than {b}\n")

elif(a<b):
    print(f"{a} is less than {b}\n")

elif(a != b):
    print(f"{a} is not equal to {b}\n")
    
#assignment operators
a= float(input("Enter the new value of a:   "))
print(f"New value of a is {a}\n")

a+=1
print("a+=1 is :   ",a)
a-=1
print("a-=1 is :   ",a)
a*=2
print("a*=2 is :   ",a)

#logical operators
if(a == 10 and b == 10):
    print("a and b have same value: ")
else:
    print("a and b have different value")