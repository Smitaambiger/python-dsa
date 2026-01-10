# Check Palindrome
# Time: O(n)

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Madam"))
