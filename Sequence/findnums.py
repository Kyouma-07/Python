#creating the function
def findnums(list1):
    list2=[]
    list3=[]
    
    for i in list1:
        if i in list2:
            list3.append(i)
        else:
            list2.append(i)
    return list3

num= int(input("Enter the size of the list: "))
list1= [0]*num
print("Enter the elements in the list: ")
for i in range(num):
    list1[i] = input()
    
a= findnums(list1)
print("Duplicate elements are:  ",a)