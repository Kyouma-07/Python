num = int(input("Enter the number to Reverse:   "))
sum =0
new_num = num
while(num!= 0):
    temp= num%10
    sum = (sum*10)+temp
    num= num//10
print(f"reverse of {new_num} is {sum}")