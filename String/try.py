s = "Hello, Hello, World!"
find_index = s.find("World")  # 13
print(find_index)
#
rfind_index = s.rfind("Hello")  # 7
print(rfind_index)
count_occurrences = s.count("Hello")  # 2
print(count_occurrences)

c= float(10/3)
d= float(10/3)

print (c)
print(d)
print ( c==d)
print( 1.5 == 1.5)


a= 65
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()