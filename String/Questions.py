import string

def get_string_length(s):
    return len(s)

def convert_to_uppercase(s):
    return s.upper()

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

def reverse_words(s):
    return ' '.join(s.split()[::-1])

def to_title_case(s):
    return s.title()

def remove_punctuation(s):
    return ''.join(c for c in s if c not in string.punctuation)

def count_characters(s):
    return {char: s.count(char) for char in set(s)}

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def replace_word(s, old_word, new_word):
    return s.replace(old_word, new_word)

def reverse_string(s):
    return s[::-1]

def find_first_non_repeating(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

def main():
    while True:
        print("\nString Manipulation Program")
        print("1. Get string length")
        print("2. Convert to uppercase")
        print("3. Check if palindrome")
        print("4. Count vowels")
        print("5. Reverse words")
        print("6. Convert to title case")
        print("7. Remove punctuation")
        print("8. Count character occurrences")
        print("9. Check if anagram")
        print("10. Replace word")
        print("11. Reverse string")
        print("12. Find first non-repeating character")
        print("0. Exit")

        choice = input("Enter your choice (0-12): ")

        if choice == '0':
            print("Thank you for using the String Manipulation Program. Goodbye!")
            break

        s = input("Enter a string: ")

        if choice == '1':
            print(f"Length of the string: {get_string_length(s)}")
        elif choice == '2':
            print(f"Uppercase: {convert_to_uppercase(s)}")
        elif choice == '3':
            print(f"Is palindrome: {is_palindrome(s)}")
        elif choice == '4':
            print(f"Number of vowels: {count_vowels(s)}")
        elif choice == '5':
            print(f"Reversed words: {reverse_words(s)}")
        elif choice == '6':
            print(f"Title case: {to_title_case(s)}")
        elif choice == '7':
            print(f"Without punctuation: {remove_punctuation(s)}")
        elif choice == '8':
            print("Character occurrences:")
            for char, count in count_characters(s).items():
                print(f"'{char}': {count}")
        elif choice == '9':
            s2 = input("Enter another string to check for anagram: ")
            print(f"Is anagram: {is_anagram(s, s2)}")
        elif choice == '10':
            old_word = input("Enter the word to replace: ")
            new_word = input("Enter the new word: ")
            print(f"After replacement: {replace_word(s, old_word, new_word)}")
        elif choice == '11':
            print(f"Reversed string: {reverse_string(s)}")
        elif choice == '12':
            result = find_first_non_repeating(s)
            if result:
                print(f"First non-repeating character: {result}")
            else:
                print("No non-repeating character found.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()