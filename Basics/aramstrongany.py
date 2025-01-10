num= int(input("Enter the number to check for armstrong: "))
new_num= num
total=0
count=0

while num!=0:
    count+=1
    num=num//10
print(f"{new_num} is a  {count} digit number: ")

num =new_num

while num!=0:
    temp=num%10
    total = total + (temp ** count)
    num=num//10
if total == new_num:
    print(f"{new_num} is an armstrong number:")
else:
    print(f"{new_num} is not an armstrong number:")