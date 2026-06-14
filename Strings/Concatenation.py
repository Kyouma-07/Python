
#1 : String concatenation :-
#strings in python are immutable :
s = "hello"
s += " world"

#python does not modify " hello" , it creates a new string " hello world "
"""
everytime we do +
# new memory is allocated
#old content is copied
# new content is appended
"""

#2 : REPEATED + is inefficient for very large string concatenations
words = ['a' , 'b' , 'c']
result = ""
for word in words:
    result += word

"""
#iteration 1 -> "a"
#iteration 2 -> "a" +"b" -> new copy
#iteration 3 -> "ab" +"c" -> new copy
TIme = 0(n^2)
"""


#3 : join()  Method
#Instead of repeatedly creating strings, we only build once
#"separator".join(iterable)
words = ["I", "love", "Python"]
result = " ".join(words)
# "I love Python"

#how join() works
"""
precalculates total size
allocates memory once
inserts elements efficiently
Time = O(n)
"""
#note:
",".join(["a", "b", "c"])   # works
",".join("abc")             # works, but different
#since strings are iterable, character wise join
#we get the output "a,b,c"
#join requires and works with strings only.


#inefficient
s = ""
for i in range(10000):
    s += str(i)

#efficient
s = "".join(str(i) for i in range(10000))



#4 : ADVANCE PATTERNS

#4.1  transform + join()
words = ["hello", "world"]
result = " ".join(word.upper() for word in words)
# "HELLO WORLD"
#upper() functions changes all to Upper case


#4.2  Filter + join()

s4 = "a1b2c3"
res = "".join( ch for ch in s4 if ch.isalpha())
#"abc"
#isalpha() functions checks whether a string is alphabet or numeric

#4.3 :  Reverse words using join + slicing
s4 = "I love Python"

temp = " ".join(s4.split()[::-1])
# "Python love I"
s4 = "Hello world from Python"
temp1 = " ".join(reversed(s4.split()))  #memory efficient option


#4.4 Chunk + join
s4 = "abcdefgh"
k = 2
chunks = [s4[i:i+k] for i in range (0 , len(s4), k)]
chunks =  "-".join(chunks)
# "ab-cd-ef-gh"


#4.5 Flatten list of string
lists = [["a", "b"], ["c", "d"]]

res2 = "".join("".join(sub) for sub in lists)
# "abcd"

#4.6
#Edge cases
" ".join([])  # ""
",".join(["hello"])  # "hello"
"-".join(["a", "b", "c"])  # "a-b-c"


#NOTE - join() ONLY ACCEPTS STRINGS


#Questions

#1: s = "abcdefg"
# take chars at even index, reverse them, then join
# output: "geca"

#2: remove consequtives
#2 : s = "aaabbccdaa"
# output: "abcda"
#Must use slicing + join

#3 : s = "abcdefg"
# output: "badcfeg"

#4 : s = "abcdefgh"
# pick 1st, last, 2nd, second-last...
# output: "ahbgcfde"

#5: s = "I love Python"
# output: "nohtyP evol I"


#PATTERNS

#1 split() + join()
#resul = "sep".join(process(x) for x in s.split(delimiter))

#2 : Removing Patterns
#2.1 Remove specific chars
s10 = "a1b2c3"
"".join(ch for ch in s10 if ch.isalpha())

#2.2 Remove substring pattern
s11 = "abcXXdefXXghi"
"".join(part for part in s11.split("XX"))

#3 : NORMALIZATION PROBLEMS
#3.1 Remove extra delimiters
s12 = "a,,b,,,c"
",".join(filter(None, s12.split(",")))
