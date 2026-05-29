

#1  controlled reversal (partial reverse)
#slicing specific parts:
s = "abcdefgh"
print(s[2:6][::-1])   # "cdef" → "fedc"

#idea => slice first and reverse that slice
#s[2:6] slice , [::-1] reverse that slice

#2 Reverse without Breaking Structure
#reverse only parts, keeping other intact:

s2 = "abcdef"
result =  s2[:2] +s2[2:5][::-1] +s2[5:]
#output = "abedcf"
#used in problem solving

#note s[ : : -1] becomes = s[-1 : -len(s)-1 : -1]


"""
| Step | Direction | Condition   |
| ---- | --------- | ----------- |
| +ve  | →         | start < end |
| -ve  | ←         | start > end |

"""

#3 Pattern:Jump Slicing(step >1)
s3 = "abcdefgh"
print(s3[::2]) #"aceg"
print(s3[1::2]) #"bdfh"


#4 Reverse Jump
s4 = "abcdefgh"
print(s4[::-2])  #"hfdb"

#5 NEGATIVE INDEX +STEP
s5 = "abcdefgh"
print(s5[-2::-2]) #"geca"

#6 Palindrome
s6 = "racecar"
mid = len(s6)//2  # 3
print(s6[:mid])       # "rac"
print(s6[:mid:-1])    # "rac"

print(s6 == s6[::-1])  #checks for palindrome

#using two-pointes
def is_palindrome_pointers(str1: str) -> bool:
    left = 0
    right = len(str1) - 1

    while left < right:
        if str1[left] != str1[right]:
            return False
        left += 1
        right -= 1

    return True

#7 CHUNKING PATTERN
s7= "abcdefgh"
chunks = [s[i:i+2] for i in range(0, len(s), 2)]  #this is list comprehension
print(chunks)
#output ['ab', 'cd', 'ef', 'gh']

#can be done as
chunks1 = []
for i in range(0,len(s7),2):
    chunks1.append(s7[i:i+2])


#8 STRING ROTATION
#81. LEFT ROTATION
s8 = "abcdef"
k = 2
print(s8[k:] + s8[:k])
"""
s[2:] → "cdef"
s[:2] → "ab"
"""

#8.2 RIGHT ROTATION
print(s8[-2:] + s8[:-2])
#"ef" + "abcd"


#9REVERSE WORDS IN A STRING
def reverse_words(s9: str) -> str:
    words = s9.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


#10 DROPPING EVERY 3rd element:
s10 = "abcdefghij"
result = ""

for i in range(0, len(s)):
    if (i + 1) % 3 != 0:
        result += s[i]

print(result)  # Output: "abdeghj"

#using enumerate ()
"""
s = "abcdefghij"
result = ""

# enumerate hands us the index (i) AND the character (char) automatically!
for i, char in enumerate(s):
    if (i + 1) % 3 != 0:
        result += char
print(result)  # Output "abdeghj"
"""

"""s = "abcdefghij"
result = "".join(s[i:i+2] for i in range(0, len(s), 3))
print(result)  # Output: "abdeghj" (Dropped 'c', 'f', 'i')
"""

#11 REPLACE VOWELS
#SOL1 USING TWO POINTERS 0(n) space.
def reverse_vowels_your_way(s11: str) -> str:
    chars = list(s11)
    vowels = set("aeiouAEIOU")
    vowel_indices = []

    for i, char in enumerate(chars):
        if char in vowels:
            vowel_indices.append(i)

    left = 0
    right = len(vowel_indices) - 1

    while left < right:
        pos1 = vowel_indices[left]
        pos2 = vowel_indices[right]
        chars[pos1], chars[pos2] = chars[pos2], chars[pos1]
        left += 1
        right -= 1
    return "".join(chars)

#SOL2 USING TWO POINTERS 0(1) space.
def reverse_vowels(s12: str) -> str:
    chars = list(s12)
    vowels = set("aeiouAEIOU")
    left = 0
    right = len(chars) - 1

    while left < right:
        if chars[left] not in vowels:
            left += 1
            continue
        if chars[right] not in vowels:
            right -= 1
            continue

        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)
