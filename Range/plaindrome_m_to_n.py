a= int(input("Enter the starting point: "))
b=int(input("Enter the ending point: "))

for i in range(a , b+1):
        new_num =i
        sum =0
        temp_i =i
        while (temp_i!=0):
            temp =temp_i%10
            sum= (sum*10)+temp
            temp_i=temp_i//10
       
        if(sum == new_num):
            print(new_num)

    
        