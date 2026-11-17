
# Palindrome Checker Project

def palindrome_check():
    text = input("Enter a word: ")

    if text == text[::-1]:
        print(text, "is a Palindrome")
    else:
        print(text, "is not a Palindrome")


palindrome_check()
