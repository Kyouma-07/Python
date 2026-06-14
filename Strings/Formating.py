#STRING FORMATTING:


#1- f-strings (String formatting)
#allows us to insert variables directly into strings

name = "John"
print(f"Hello {name}")

"""
Before f-strings, formatting was messy and unreadable.
Python introduced f-strings to:
improve readability
reduce bugs
make code clean.

usage : - 
whenever we need to print variables with text
Logging , output formatting, user messages
"""

#Features
#1.1 : we can  use expression inside strings
a = 5
b = 3
print(f"Sum = {a + b}")  # Sum = 8

#1.2 :  function call inside strings
name = "john"
print(f"{name.upper()}")  # JOHN

#1.3 Formatting numbers / Float precision
pi = 3.14159
print(f"{pi:.2f}")  # 3.14

#1.4 Width and alignment
text = "hi"
print(f"{text:>10}")  # right align
print(f"{text:<10}")  # left align
print(f"{text:^10}")  # center

#1.5 Padding
num = 7
print(f"{num:03}")  # 007

#1.6 debugging
x = 10
print(f"{x=}")  # x=10


#2 : .format() METHOD

name = "John"
age = 25
print("My name is {} and I am {}".format(name, age))

#before f-strings this was the cleanest method.

#2.1 : Features

#Positonal Arguments
print("Hello {} {}".format("John", "Doe"))

#Index Based
print("{1} {0}".format("John", "Doe"))  # Doe John

#Named Arguments
print("Name: {n}, Age: {a}".format(n="John", a=25))

#Formatting Numbers
pi = 3.14159
print("{:.2f}".format(pi))  # 3.14

#Alignment
print("{:>10}".format("hi"))

"""
used in older codebases
when f-strings are not available
more typing and less readable
"""


#3 : % FORMATTING (OLD STYLE)
name = "John"
age = 25
print("My name is %s and I am %d" % (name, age))

#insipred by C, old python used this.
#Specifiers  %s = string , %d = integers , %f = float

pi = 3.14159
print("%.2f" % pi)  # 3.14

"""
Legacy systems use this
Error Prone
Hard To Read
Limited Flexibility
"""


#4 : STRING CONCATENATION (+)
name = "John"
print("Hello " + name)

#used for basic string joining
#why bad ?  : ->
#print("Age: " + age)  # ERROR
#needs conversion:
print("Age:" + str(age))

"""
unreadable with many variable
type errors
messy
%never use to format strings, only for basics joining
"""

#5 : Multiple Variables & Complex Formatting
name = "John"
score = 92.456
print(f"{name} scored {score:.1f} marks")
#John scored 92.5 marks


#6 :  Escaping Braces
print(f"{{Hello}}")
#output = {Hello}

#7 : Format Specifiers
#general structure : {value:format}

#7.1 : Decimal Places
f"{3.14159:.2f}"  # 3.14  > .2f describes format till 2 places only

#7.2 :  Width
f"{10:5}"  # '   10'

#7.3 : Zero Padding
f"{5:03}"  # 005

#7.4 : Alignment
f"{'hi':^10}"  # centered

#note : use f string most of the times.
name = "John"
age = 25

"""
f"{name} is {age}"              #best
"{} is {}".format(name, age)   #OK
"%s is %d" % (name, age)        #OLD
"Name: " + name                 #BAD
"""

