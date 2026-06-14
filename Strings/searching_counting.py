#1 : .find() function
#syntax = string.find(substring, start, end)

word = "python programming"
print(word.find("pro"))
# Output: 7

"""
scans a string from left to right to locate a specific substring.
Returns the lowest index (starting  position) where substring is found.
Safely returns -1 if the substring is completely absent.
"""
#USE-CASE --> checking pattern exists when its absence is a normal, expected possibility in logic flow.
#example - safe URL parsing , extracting domains where URL's dont have www.

#EDGE-CASE:
#1.1: Searching an empty string, returns 0 always , python considers "" to exist at the very beginning of every string.
print("hello".find(""))
# Output: 0

#1.2: Out of Bound index: searching with an index larger than the string itself, doesn't crash with IndexError, it returns -1
print("abc".find("a", 100))
# Output: -1


#2 :  .index() function
#syntax : string.index(substring, start, end)
data = "user_id: 9942"
print(data.index(":"))
# Output:

"""
Operates almost identically to .find(), scanning left to right.
If the substring is not found, it strictly raises a ValueError exception.
"""
#USE-CASE --> Strict data validation where a missing substring means the data is corrupted, and the program must stop processing.
#EXAMPLE :  Strict data validation where a missing substring means the data is corrupted, and the program must stop processing.

#EDGE-CASE:
#2.1: The Empty String in an Empty String: Just like .find(), searching for "" returns 0. Even if the parent string is also empty!
print("".index(""))
# Output: 0


#3  :   .rfind() (Reverse Find)
#syntax :  string.rfind(substring, start, end)
path = "C:/users/admin/report.pdf"
print(path.rfind("/"))
# Output: 14

"""
Scans the string from right to left (backwards).
Returns the highest index (the very last occurrence) of the substring. Returns -1 if not found.
"""
#USE-CASE --> Extracting the end portion of a dynamic string, like isolating a file name from a long, unpredictable folder path.
#EXAMPLE :  File Name Extraction: Users upload files from different operating systems (Mac/Windows). .rfind("/") guarantees you always slice right before the actual file name, ignoring the varying folder depths.

#EDGE-CASE:
#3.1:   Empty String Reversal: While .find("") returns 0, .rfind("") returns the absolute end of the string (its length)
print("hello".rfind(""))
# Output: 5

#3.2:   Overlapping Options: If there are overlapping matches, it strictly grabs the start index of the last valid one.
print("aaaa".rfind("aa"))
# Output: 2 (Matches the 'aa' at index 2 and 3)


#4: .count() function
#syntax:    string.count(substring, start, end)
binary = "101010"
print(binary.count("10"))
# Output: 3

"""
Calculates the total frequency of a substring inside a parent string.
Uses a non-overlapping sliding pointer (jumps completely past a match before looking for the next).
"""

#USE-CASE:  Keyword density tracking, or validating the exact number of delimiters in a data string (like commas in a CSV).
#EXAMPLE:   CSV Validation: Before processing a line from a database export that should have 5 columns, you use row.count(",") to ensure there are exactly 4 commas.

#EDGE-CASE:
#4.1:   The Overlap Blindspot: Because it jumps past matches, it will undercount overlapping sequences.
print("aaaa".count("aa"))
# Output: 2

#4.2:   Counting the Void: If you ask it to count empty strings "", it counts the invisible boundaries between every single character, returning Length + 1.
print("abc".count(""))  # Output: 4


#5: .startswith() function
#syntax:    string.startswith(prefix_string_or_tuple, start, end)
status = "ERROR: Timeout"
print(status.startswith("ERROR"))  # Output: True

"""
Evaluates if a string strictly begins with a specific pattern, returning True or False.
Can accept a tuple of multiple strings to check several prefixes at once.
"""

#USE-CASE:  Routing, filtering, or categorizing strings based on their prefix without using memory-heavy string slicing.
#EXAMPLE:   Log Routing: You use if log.startswith(("[WARN]", "[ERROR]")): to instantly filter out harmless info messages and route only critical alerts to a dashboard.

#EDGE-CASE:
#5.1:   The List Trap: If you pass a list instead of a tuple to check multiple items, Python will crash.
# print("text".startswith(["a", "t"])) #  TypeError!
print("text".startswith(("a", "t")))   # Valid

#5.2:   Empty Prefix: Asking if a string starts with "" will always evaluate to True.
print("text".startswith("")) #True


#6: .endswith() function
#syntax:   string.endswith(suffix_string_or_tuple, start, end)
filename = "profile_pic.png"
print(filename.endswith((".png", ".jpg")))  #

"""
Evaluates if a string strictly finishes with a specific pattern, returning True or False.
Anchors the check to the very end of the string.
"""

#USE-CASE:  File type validation and suffix filtering.
#EXAMPLE:   Upload Security: You are building an image uploader. You use .endswith() to ensure a file strictly ends with a valid image extension to prevent users from uploading malicious .exe scripts.

#EDGE-CASE:
#6.1:   The Empty Tuple Trick: If you pass an entirely empty tuple (), it will always return False because there is nothing to match against.
print("data.csv".endswith(()))  # Output: False


#7: in operator (membership testing)
#syntax:
#substring in string (Returns True or False)
#substring in string (Returns True or False)

phrase = "Python is beautiful"
print("thon" in phrase)      # Output: True
print("Java" not in phrase)  # Output: True
"""
This isn't a method; it's a built-in Python operator. It performs a boolean check to see if a substring exists anywhere inside a parent string.
It is heavily optimized in C under the hood. If you only need to know if something is there, and you don't care where it is (index), this is the fastest and most readable way to do it.
"""
#USE-CASE:  Quick boolean checks for conditions, filters, or if/else branching.

#EDGE-CASE:
#7.1 :The Empty String Ghost: Just like .find(), asking if an empty string is inside another string is always logically True.
print("" in "hello")  # Output: True

#7.2:   Strict Case Sensitivity: The in operator is mercilessly case-sensitive. "Admin" in "admin_user" is False. You must normalize casing first if you want a safe check.


#8: .rindex() (Reverse Index)
#syntax:    string.rindex(substring, start, end)
data = "version_1.0_final"
print(data.rindex("_"))  # Output: 11

"""
Scans the string from right to left (backwards) to find the highest index.
If the substring is completely absent, it strictly raises a ValueError exception.
"""

#USE-CASE:  Strict data validation from the rear of a string where a missing target means the data is fatally corrupted.
#EXAMPLE:   Strict Extension Parsing: You have a strict database of filenames where every file must have a period (.). Using .rindex(".") guarantees you find the last dot to extract the extension. If a corrupted entry without a dot slips in, the ValueError stops the bad data from processing.

#EDGE-CASE:
#8.1:   Strict Extension Parsing: You have a strict database of filenames where every file must have a period (.). Using .rindex(".") guarantees you find the last dot to extract the extension. If a corrupted entry without a dot slips in, the ValueError stops the bad data from processing.
print("hello".rindex("z")) #ValueError: substring not found



"""
5 Basic Questions (Syntax & Operations)
Write a line of code using .find() to locate the first occurrence of "@" inside the string email = "user@domain.com".

What will print("hello world".index("z")) output or trigger?

What is the exact numerical output of "hahaha".count("ha")?

Write a boolean evaluation using .endswith() to check if doc = "report.PDF" ends with ".pdf". (Hint: Account for case sensitivity first!)

Write a boolean expression using the in operator to check if the exact word "admin" is present in the string "system_admin_123".

🧠 10 Fundamental Logic Questions (Scenarios & Algorithms)
The Readability Check: Explain why a senior developer would prefer you to write if "error" in log_string: instead of if log_string.find("error") != -1:.

Reverse Extraction: Given path = "/usr/local/bin/python", explain how you would use .rfind() alongside basic string slicing to dynamically extract just the file name ("python") regardless of how many folders are in the path.

Strict Data Validation: You are writing a parser that expects a string formatted exactly like "ID:12345". Explain why data.startswith("ID:") is safer and faster than slicing it like data[:3] == "ID:".

The Tuple Trap: A junior developer writes if word.startswith("A", "E", "I", "O", "U"): to check for vowels. Why will this crash, and what is the exact syntax to fix it?

Targeted Bounded Search: Given text = "The cat in the hat", write an expression using .find() that searches for the word "cat" but only begins its search from index 5. What value will it return?

Counting Inversions: If you have s = "10101010", what is the exact difference in the output between s.count("10") and s.count("01")? Explain why based on Python's non-overlapping pointer.

Safe Fallback Retrieval: You need to slice a string up to the character "-". If the "-" doesn't exist, you want to return the whole string. Explain how .find() handles the missing character to allow this to fail safely.

The Empty Ghost: What happens if you search for an empty string using .index("") inside "hello"? Does it crash, or does it return a specific index?

The Right-to-Left Dilemma: In the string sentence = "I like apples, apples are good", what index does .rindex("apples") return compared to .index("apples")?

Case-Insensitive Counting: Given feed = "Breaking news: BREAKING glass heard.", write a single line of code to count exactly how many times the word "breaking" appears, ignoring all casing rules.

📝 20-Question Daily Quiz
What value does "python".find("z") return?

A) None

B) 0

C) -1

D) Raises ValueError

Which method should be used if the absence of a substring is considered a critical program error that must stop execution?

A) .find()

B) .count()

C) .index()

D) .startswith()

What does "banana".count("ana") evaluate to?

A) 1

B) 2

C) 3

D) 0

Which data structure is explicitly required to pass multiple prefix arguments into .endswith()?

A) List

B) Dictionary

C) Set

D) Tuple

What is the output of "hello".find("")?

A) -1

B) 0

C) 5

D) Raises ValueError

What does "apple".rfind("p") return?

A) 1

B) 2

C) 0

D) -1

What happens if you execute "hello".rindex("z")?

A) Returns -1

B) Returns None

C) Raises ValueError

D) Returns 0

Why is .startswith() preferred over string[:len(target)] == target for boundary checks?

A) It mutates the string securely.

B) It is case-insensitive by default.

C) It completely avoids creating temporary slice objects in memory.

D) It supports Regex under the hood.

What is the output of "xxx".count("xx")?

A) 2

B) 1

C) 3

D) 0

If s = "testing", what does s.count("") return?

A) 0

B) 7

C) 8

D) 1

How does the in operator handle case sensitivity?

A) It ignores case automatically.

B) It strictly enforces case sensitivity.

C) It throws a TypeError on mixed cases.

D) It converts everything to lowercase before checking.

What does "file.txt".endswith(".TXT".lower()) evaluate to?

A) False

B) True

C) None

D) Raises TypeError

If path = "/users/admin/docs", what does path.find("/") return?

A) 0

B) 1

C) 6

D) 12

Using the exact same path from question 13, what does path.rfind("/") return?

A) 0

B) 6

C) 12

D) 17

What occurs when .endswith() is provided an entirely empty tuple () as its argument?

A) Returns True

B) Returns False

C) Raises ValueError

D) Raises TypeError

If text = "abracadabra", what is the output of text.count("a", 1)?

A) 5

B) 4

C) 3

D) 0

What is the fundamental difference between .index() and .rindex()?

A) .index() raises an error; .rindex() safely returns -1.

B) .index() scans left-to-right; .rindex() scans right-to-left.

C) .index() counts overlapping strings; .rindex() does not.

D) There is absolutely no difference; they are aliases.

What does "   ".count(" ") evaluate to?

A) 0

B) 1

C) 2

D) 3

Given string = "algorithm", what does string.startswith("algo", 0, 3) evaluate to?

A) True

B) False

C) Raises IndexError

D) Returns 0

Which of the following is the fastest, most Pythonic way to check if the word "error" is present anywhere inside a string named log?

A) log.find("error") != -1

B) log.count("error") > 0

C) "error" in log

D) log.index("error")
"""