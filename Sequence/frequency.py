#creating function
def frequency(str1):
    dict1 = {}
    newstr = str1.split()
    
    for i in newstr:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1
    return dict1

str1 =str(input("Enter the string:  "))
a= frequency(str1)
for key,value in a.items():
    print(key+" : ",value)