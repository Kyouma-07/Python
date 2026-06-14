#STRING COMPARISON

#1:  Equality
a = "hello"
b = "hello"

print(a == b)   # True
print(a != b)   # False

#note: "Hello" != "hello", python is case sensitive

#2: Lexicographical Comparison
print("apple" < "banana")   # True
print("zebra" > "apple")    # True

#uses ASCII internally
#Python compares character by character using ASCII:
print("Zebra" < "apple")   # True  #z = 90 , a = 97 in ASCII

#"bat" > "ball"
"""
Compare step-by-step:
b == b → move
a == a → move
t > l → True """

#2.1 Length Impact
print("app" < "apple")  # True
#shorter string is smaller if prefix are same

#2.2 Comparison After Normalization
a = "  Hello "
b = "hello"

if a.strip().lower() == b.strip().lower():
    print("Equal")

#2.3 Membership Comparison( in , not in)
print( "he" in "hello")  #True
print( "x" not in "hello") #True

#2.4 Comparing Multiple Strings
names = ["banana", "apple", "cherry"]
print(sorted(names))
#['apple', 'banana', 'cherry']

#2.5: Prefix checking
word = "something"
if word.startswith("so"):
    print("True")
#word.endswith("suffix") to check for suffix

#3: CASE SENSITIVITY/ CONVERSION & NORMALIZATION
#Real-world data is messy. Always clean it.

#3.1 :  .lower()
print("HELLO".lower())
#hello
#syntax  string.lower()

#3.2 : .upper()
#syntax = string.upper()
print("hello".upper())

#3.3 : .capitalize()
#syntax = string.capitalize()
print("hello world".capitalize())
#note: only first character capitalize

#3.4 : .title()
#syntax = string.title()
print("hello world".title())

#3.5 : Title Edge Case
print("john's book".title())
#output: # "John'S Book"

#3.6 : .swapcase()
print("hello".swapcase())
#hELLO
#syntax = string.swapcase()

#3.7 : .casefold()
print("ß".lower())  #already lower case so returns the same output
print("ß".casefold()) #ss , turns it into its phonetic sound, better than lower()

#3.8 : Normalization
text = " homba homba romba rombaa"
clean = text.strip().lower()

#remvoes spaces
#make lowercase

#4 : WHITESPACE HANDLING
"""
Whitespace = invisible characters:
" " → space
"\t" → tab
"\n" → newline
"""

#4.1  .strip()
s = "   hello   "
print(s.strip())   # "hello"
#remove all whitespace from both ends only (NOT middle)
print("  hello  world  ".strip())
#output "hello world"

#Logic -> starts from left - remove whitespace
#       -> starts from right - remove whitespace
#       stop when first non-whitespace char appears

#4.2 :  paramterized strip() or custom strip()
print("***hello***".strip("*"))
#output "hello"

#note:
print("xyxhellozyx".strip("xyz"))
#output: "hello"
#it removes any of those characters from both left and right , not the exact string "xyz"

#4.3 :  .lstrip()
#remove only from left
print("   hello   ".lstrip())
#output : "hello   "
#usecase : when alignment matters:
line = "    data"
clean1 = line.lstrip()

#4.4 : .rstrip()
#removes from RIGHT only
print("   hello   ".rstrip())
#output :  "    hello"

#usecase : when reading files (removing newline)
line = "hello\n"
clean2 = line.rstrip()

#4.5   .split()
#strip() cannot remove whitespace b/w lines , thats why we use .split()
#.split() breaks down the string into a list of  substrings.
s = "hello     world"
print(s.split())
#output ['hello', 'world']


s = "   hello    world   "
clean3 = " ".join(s.split())
print(clean)
#output "hello world"


#notes:  



