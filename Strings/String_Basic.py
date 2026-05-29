#1  A string is just text data enclosed in quotes:

s1 = " hello "
s2 = " world "


#2  Indexing  (Accessing Characters )

s = "python"
print(s[0])  #p
print(s[3])  #h
print(s[-1]) #n  -1 gives reverse index


#3  string slicing   ( to divide or slice a given string according to our need)

string1 =  "python"
print(s[0:4])   # pyth
print(s[:3])    # pyt
print(s[3:])    # hon

"""
s[start : end]
→ includes start
→ excludes end
"""

#4  reversing a string
string2 = "python"
print(string2[::-1])

"""  string[start:end:step]  , step -1 => reverse, note: start, end are indexes not positions """

#5 String Immutability
""" once a string is created. it cannot be changed and its content cannot be modified directly 
any operations that appears to modify a string actually creates a new string object 
string operations return a new string with modified changes """

s5= "hello"
s5[0] = "H"   #cannot be done

#instead we use
s5 = "hello"
s5 = "H" + s5[1:]
print(s)   # Hello

#=> creating modified strings actually creates a new string => "H" + s[1:] is assigned to variable "s" now

#6 Multi lined strings
s6 = (""" hello
      world""")

#7 STRING OPERATIONS
#operation1   STRING LENGTH  & COMPARISON

#1.1 len(string)
#Returns numbers of character in a string
op1 = "python"
print(len(op1))

#using a for loop
count = 0
for  i in op1:
    count += 1
print(count)
#note: -> space are counted, special characters as well, empty string has a len of 0
#all escape sequence characters take 1 len each

#1.2 Lexicographical comparison
#Python compares strings character by character using UNICODE values
print("abc" < "abd")   # True
print("abc" > "ab")    # True
#NOTE : - case matters
print("apple" > "Banana")   # True
#'a' (97) > 'B' (66)

#1.3 ORD() function
#we use the ord function to check their UNICODE values
print(ord('a'))  # 97
print(ord('B'))  # 66

#1.4 EQUALITY OPERATOR (==)
#checks value(content of the variable) returns true or false
a = "hello"
b = "hello"
print(a == b)   # True
#note: == operator is case-sensitive
print("Hello" == "hello")   # False
#always use == operator for comparing string values

#1.5 is OPERATOR (identity)
#checks MEMORY (same object or not)
a = "hello"
b = "hello"

print(a is b)   # True (maybe)

a = "hello world"
b = "hello world"

print(a is b)   # may be False

#THIS HAPPENS TO DUE TO STRING INTERNING

#1.6 STRING INTERNING
#python reuses memory for some strings to optimize performance
#small strings are automatically interned , identifiers too
a = "hello"
b = "hello"
print(a is b)   # True

#but
a = "".join(["he", "llo"])
b = "hello"
print(a == b)   # True
print(a is b)   # False
#same value , different memory

#forced interning
import sys
a = sys.intern("hello world")
b = sys.intern("hello world")
print(a is b)   # True

a = "py" + "thon"
b = "python"
print(a == b)   # True
print(a is b)   # may be True or False