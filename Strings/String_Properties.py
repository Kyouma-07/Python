#:  STRING PROPERTIES:

#1: .isaplha()
#These methods evaluate the structural identity of a string. They don't change anything; they strictly return a boolean (True or False) by checking every single character.
#checks if all chars in string are alphabets:
#Syntax:    string.isaplha()

print("Python".isalpha())   # True
print("Python3".isalpha())  # False (The '3' breaks it)

#Use-case: Validating a user's first or last name to ensure they didn't type numbers or symbols.
#example:   If you are building a profile generator, you use if name.isalpha(): to prevent users from making their first name "xX_Sniper_Xx"

#EDGE-CASE:
#1.1:   spaces are not letters.
print("John Doe".isalpha()) #False

#1.2:   empty strings always return False because there is no alphabet present to validate.
print("".isalpha()) #False



#2: .isdigit()
#checks is all the chars in string are digits(0-9)
#use-case:  Safely verifying user input before converting it with int() to prevent your program from crashing.
#syntax:    string.isdigit()
#note:  allows subscripts and such. (like  1^2)

print("2026".isdigit())  # True
print("20 26".isdigit()) # False (Space breaks it)

#example:   When asking a user for their account PIN: if pin.isdigit() and len(pin) == 4:

#EDGE-CASE:
#2.1:    Floats return false:
print("3.14".isdigit()) #False , cause . "period" is not a digit

#2.2:   -ve number strings return False:
print("-50".isdigit())  #false, because - is math symbol.



#3: .isalnumn()
#: Checks if all characters are alphanumeric (letters OR numbers). It is basically .isalpha() and .isdigit() combined.
#Use-case: Validating usernames or strict password criteria.
#syantax:   string.isalnum()

print("Admin2026".isalnum())  # True
print("Admin_2026".isalnum()) # False (The underscore breaks it)


#4:  .isspace()
#:  Explanation: Checks if the string consists entirely of whitespace characters (spaces, tabs \t, newlines \n).
#use-case:  Use-case: Detecting "empty" form submissions where a user just hit the spacebar a few times to bypass a required field.
#syntax:    string.isspace()

print("   \n \t".isspace())  # True

#5:   .isnumeric()
#:  broader check, allows everything above plus fractions.
#Use-case: when we want to check for any numerical values:
#syntax:    string.isnumeric()

print("½".isnumeric()) #True
#example:- used when parsing natural human text containing fractions

#6: .isdecimal()
#explanation:    only allows standard Base10 (0-9) , no subscripts
#use-case:  used for strict database IDs
#syntax:    string.isdecimal()

fraction = "½"
print(fraction.isdecimal())  # False
print(fraction.isdigit())    # False
print(fraction.isnumeric())  # True


#6: .isidentifier()
#explanation:   Checks if a string is a valid Python variable name (must start with a letter/underscore, followed by letters/numbers/underscores).
#Use-case: Metaprogramming (scripts that dynamically generate Python code).
#syntax:    string.isidentifier()

print("_my_var1".isidentifier())  # Output: True

#EDGE-CASE:
# It does NOT check for reserved keywords!
print("def".isidentifier())    # Output: True (Even though 'def' is restricted)
print("class".isidentifier())  # Output: True


##: ADVANCE SPLITTING, PARTITIONING & JOINING

#1: .split()
#explanation:- : Breaks a string into a List of smaller strings based on a delimiter.
#Use-Case:  Parsing CSV files or breaking sentences into words.
#syntax:    string.split(separator= Nne, maxsplit = -1)

csv_row = "apple,banana,orange"
print(csv_row.split(","))
# Output: ['apple', 'banana', 'orange']

# Extracting a domain from an email
email = "user@company.com"
domain = email.split("@")[1]
print(domain)  # Output: "company.com"

#EDGE-CASE:
# Consecutive delimiters create empty strings
print("a,,b".split(","))  # Output: ['a', '', 'b']

# Default splitting (no args) ignores extra spaces
print("a   b".split())    # Output: ['a', 'b']


#2: .rsplit()
#explanation:   operates exactly like .split(), but scans from right side.
#Use-Case:   isolating the file name from a pth while keeping the rest intact.
#syntax:    string.rsplit(seperator = None , maxsplit =-1)

path = "C:/users/admin/file.txt"
# Split only on the very last slash
print(path.rsplit("/", maxsplit=1))
# Output: ['C:/users/admin', 'file.txt']


#3: .splitlines()
#explanation:   specifically spilts a string at line boundaries( \n,\r,\r\n).
#use-case;   parsing massive multi-line texts files or raw HTTP payloads.
#syntax:     string.splitlines(keepends= False)

text = "Line1\nLine2\nLine3"
print(text.splitlines())
# Output: ['Line1', 'Line2', 'Line3']


#4 .partition() & .rpartition()
#explanation:   scans for a seperator and strictly breaks the string into exactly a 3-item Tuple: (everything_before, the_separator, everything_after)
#.rpartition() does it from the right:
#syntax:    string.partition(seperator)

header = "Host: www.google.com"
key, sep, value = header.partition(": ")
print(key)    # Output: "Host"
print(value)  # Output: "www.google.com"

#EDGE-CASE:
# If the separator isn't found, it returns the string and two empty strings
print("apple".partition("-"))
# Output: ('apple', '', '')


#5: .join()
#explanation:    takes and iterables of strings(like a list) and glues them together. The string you call it on acts as the glue.
#use-case:  building file paths or high performance concatenation.
#syntax:    seperator.join(iterable)

words = ["Python", "is", "fast"]
print("-".join(words))  # Output: "Python-is-fast"

# Dynamically generating a CSV row
user_data = ["John", "Admin", "Active"]
csv_line = ",".join(user_data)
print(csv_line)  # Output: "John,Admin,Active"


#EDGE-CASE:
# The Type Error Crash: Lists must contain ONLY strings
# print("-".join(["ID", 42]))  ❌ TypeError!

# Correct way: Cast to string first
print("-".join(["ID", str(42)]))  # Output: "ID-42"


# Replacement, Translation & Affix Removal
#1 :    .replace()
#explanation:    Substitutes occurrences of an "old" substring with a "new" substring.
#use-case:  Sanitizing data or removing dashes from phone numbers

#syntax:   string.replace(old, new[, count])

text = "bad code is bad"
# Replace only the first occurrence
print(text.replace("bad", "good", 1))
# Output: "good code is bad"

#edge-case:
# Replacing an empty string injects the new string at every boundary
print("abc".replace("", "-"))  # Output: "-a-b-c-"


#2: .maketrans() & .translate()
#explanation:   Highly optimized C-level duo. .maketrans() builds a mapping dictionary, and .translate() swaps/deletes individual characters massively all at once.
#use-case:  Stripping out multiple punctuation marks simultaneously or building ciphers.
#syntax:   table = str.maketrans(chars_to_replace, replacements, chars_to_delete)
#string.translate(table)

# Swap 'a'->'1', 'e'->'2', and DELETE 'x'
table = str.maketrans("ae", "12", "x")
text = "an excellent example"

print(text.translate(table))
# Output: "1n 2c2ll2nt 2mpl2"

#EDGE-CASE:
# The first two arguments MUST be the exact same length
# table = str.maketrans("abc", "12")  ValueError!

# Justification & Padding
#1: .zfill()
#explanation:   ":zero fill". Pads a string on the left with 0 s until it reaches the specified length.
#use-case:  Formatting binary numbers or strict database IDs.
#syntax:    string.zfill(width)

print("42".zfill(5))  # Output: "00042"

#edge-cases:
# It mathematically understands negative signs!
print("-42".zfill(5))  # Output: "-0042" (Not "00-42")


#2: .ljust(), .rjust(), .center()
#explanation:   pads a string with a specified character to align it left, right, or center within a specified width.
#use-case:  Formatting terminal outputs or log files cleanly.
#syntax:    string.center(width, fillchar)

print("ERROR".center(15, "-"))  # Output: "-----ERROR-----"
print("Data".ljust(10, "."))    # Output: "Data......"


#   ENCODING AND DECODING
#1: .encode()
#explanation:    translates human readable unicode strings into a raw machine bytes.
#use-case:  hashing passwords or sending texts over a network socket.
#syntax:    string.encode(encoding ="utf-8", errors ="strict")

text = "Café"
byte_data = text.encode("utf-8")

print(byte_data)
# Output: b'Caf\xc3\xa9' (The 'b' prefix means bytes)

#EDGE-CASE:
# Encoding foreign characters into restrictive ASCII crashes
# "Résumé".encode("ascii")  UnicodeEncodeError!

#2: .decode()
#explanation:  Translates raw machine Bytes back into a human-readable String.
#use-case:  Use-case: Reading API payloads or decoding scraped data.
#syntax:    bytes_object.decode(encoding="utf-8", errors="strict")

raw_bytes = b'Caf\xc3\xa9'
restored_text = raw_bytes.decode("utf-8")

print(restored_text)  # Output: "Café"

#Edge-cases:
# If bytes are corrupted, gracefully handle it
bad_bytes = b'Data\xff'

print(bad_bytes.decode("utf-8", errors="ignore"))   # Output: "Data"
print(bad_bytes.decode("utf-8", errors="replace"))  # Output: "Data"

"""
1. What is the output of "a   b   c".split() (with absolutely no arguments)?

A) ['a', ' ', ' ', ' ', 'b', ' ', ' ', ' ', 'c']

A) ['a', 'b', 'c']

C) ['a', '', '', 'b', '', '', 'c']

D) Raises a TypeError

2. Look at this code: "-".join(["ID", 42]). What happens?

A) Returns "ID-42"

B) Returns "ID42"

C) Raises a TypeError

D) Returns "-ID-42-"

3. What does "ab".replace("", "-") return?

A) "-a-b-"

B) "a-b"

C) "-ab-"

D) ""

4. If data = "root_admin", what does data.partition(":") return?

A) ('root_admin', '', '')

B) ('root', '_', 'admin')

C) Raises a ValueError

D) ('root_admin')

5. What does "def".isidentifier() evaluate to?

A) False, because def is a reserved keyword.

B) True, because it follows the syntactical rules for a variable name.

C) Raises a SyntaxError.

D) None

6. What is the output of "1,2,,3".split(",")?

A) ['1', '2', '3']

B) ['1', '2', ',', '3']

C) ['1', '2', '', '3']

D) ['1', '2', ' ', '3']

7. What does "-9".zfill(4) evaluate to?

A) "00-9"

B) "-009"

C) "0-09"

D) "-900"

8. Why is str.maketrans() and .translate() preferred over chaining .replace() multiple times?

A) .translate() can accept lists instead of strings.

B) .translate() operates at the C-level, substituting all mapped characters in a single pass across the string.

C) .replace() cannot be used inside loops.

D) .translate() permanently mutates the original string in memory.

9. What happens if you execute "Café".encode("ascii")?

A) Returns b"Cafe" (it automatically strips the accent).

B) Returns b"Caf\xc3\xa9".

C) Raises a UnicodeEncodeError.

D) Returns b"Caf?".

10. Why did Python 3.9 introduce .removesuffix("txt") when .rstrip("txt") already existed?

A) .rstrip("txt") only works on whitespaces.

B) .rstrip("txt") treats "txt" as a set of characters ('t', 'x') and will strip any of them from the end until it hits a non-matching character.

C) .removesuffix() modifies the string in place.

D) They are completely identical; it was just a naming update.

11. Which method would evaluate to True for the fraction "¾"?

A) .isdecimal()

B) .isdigit()

C) .isnumeric()

D) All of the above.

12. What causes str.maketrans("abc", "12") to crash with a ValueError?

A) Numbers cannot be used as replacements.

B) The first two string arguments must be the exact same length.

C) "abc" contains vowels.

D) The third argument (characters to delete) is mandatory.

13. What is the output of "A\nB".splitlines(keepends=True)?

A) ['A', 'B']

B) ['A\n', 'B']

C) ['A\n', '\nB']

D) ['A\nB']

14. What does "John Doe".isalpha() evaluate to?

A) True

B) False (because of the space).

C) False (because of the capital letters).

D) Raises a ValueError.

15. What does "".isspace() evaluate to?

A) True

B) False (there are no spaces present to validate).

C) None

D) 0

16. What prefix dictates to the Python interpreter that a string is composed of raw machine bytes rather than Unicode characters?

A) r"..."

B) f"..."

C) b"..."

D) u"..."

17. What does bad_bytes.decode("utf-8", errors="ignore") do if it hits a corrupted byte?

A) It crashes immediately.

B) It replaces the corrupted byte with a ?.

C) It silently deletes the corrupted byte and decodes the rest.

D) It returns None.

18. What is the output of "A-B-C-D".rsplit("-", maxsplit=1)?

A) ['A', 'B', 'C', 'D']

B) ['A-B-C', 'D']

C) ['A', 'B-C-D']

D) ['A-B', 'C-D']

19. What does "password123!".islower() evaluate to?

A) False (because numbers and symbols are not lowercase).

B) True (it checks the alphabetic characters and ignores the rest).

C) None.

D) Raises a TypeError.

20. What is the output of "woohoo".replace("o", "a", 2)?

A) "waahaa"

B) "waahoo"

C) "woohaa"

D) "woohoo"

5 Basic Syntax Drills
Write a single line of code to check if the string var_name = "2nd_place" is a mathematically/syntactically valid Python variable name.

Given data = "Error: System Halt", write the exact code using .partition() to split it into a 3-part tuple using ": " as the separator.

Write the code using a modern Python 3.9+ method to safely remove the exact prefix "bot_" from the string user = "bot_crawler".

You have a string binary = "101". Use .zfill() to pad it with zeros so its total length is 8 characters.

Write the exact code to encode the string "Data" into raw ASCII bytes.

🧠 10 Fundamental Logic Questions
The Numeric Matrix: Explain exactly why "¾".isdigit() evaluates to False, but "¾".isnumeric() evaluates to True.

Reverse Splitting Logic: You have a file path "C:/docs/images/pic.png". Explain why path.rsplit("/", maxsplit=1) is a more efficient and safer choice than path.split("/") if your only goal is to separate the directory from the filename.

Partition Failure State: If you execute "hello".partition("-"), what is the exact 3-item tuple that is returned since the hyphen does not exist in the string?

The Affix vs. Strip Bug: A junior developer uses "TaskRunner".rstrip("Runner") to try and extract the word "Task". Explain exactly why this creates a bug, what it actually outputs, and which method they should have used instead.

Consecutive Delimiters: If you have the string text = "a,,b", what is the exact list output of text.split(",")?

Negative Padding: Look at "-5".zfill(4). Explain why this correctly outputs "-005" instead of accidentally outputting "00-5".

Performance Architecture: You need to strip commas, periods, exclamation marks, and question marks (,.!?) from a massive 10MB text file. Why is .translate() structurally superior to chaining four .replace() methods together?

The Empty Replace Trap: What is the exact string output when you execute "abc".replace("", "-")?

Translation Constraints: A developer writes table = str.maketrans("abc", "12") to swap characters. Why will this instantly crash with a ValueError?

Graceful Network Degradation: You receive a raw byte string b"User\xffData" from a network socket, but the \xff byte is corrupted and invalid. Explain how you would write your .decode() call to ensure the script doesn't crash, but instead replaces the broken byte with a placeholder symbol (like ?).
"""