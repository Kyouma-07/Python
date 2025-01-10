#armstrong for a 3 digit number version
num = int(input("Enter the number to check for armstrong:   "))
sum =0
new_num = num
while(num!= 0):
    temp= num%10
    sum = sum+ (temp*temp*temp)
    num= num//10
if(sum == new_num):
    print(f"{new_num} is an armstrong number")
else:
    print(f"{new_num} is not armstrong number")