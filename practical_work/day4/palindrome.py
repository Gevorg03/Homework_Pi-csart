"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers."""

def palindrome(s: str):
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")
    s = s.lower()
    print(s)
    if s == s[::-1]:
        return True
    return False
print(palindrome("A man, a plan, a canal: Panama"))
