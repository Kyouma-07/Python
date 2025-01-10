num = int(input("Enter the number to check for palindrome:   "))
sum =0
new_num = num
while(num!= 0):
    temp= num%10
    sum = (sum*10)+temp
    num= num//10
if(sum == new_num):
    print(f"{new_num} is an palindrome number")
else:
    print(f"{new_num} is not palindrome number")