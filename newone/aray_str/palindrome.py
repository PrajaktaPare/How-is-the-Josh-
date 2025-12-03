import string

def is_palindrome(s):
    # Keep only alphanumeric characters and convert to lowercase
    s = ''.join(ch.lower() for ch in s if ch.isalnum())

    # Compare string with its reverse
    return s == s[::-1]

# Examples
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
