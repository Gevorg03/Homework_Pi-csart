"""Given a string s consisting of words and spaces, return the length of the last word in the string."""

def last_word_len(s: str):
    s = s.split(" ")
    for el in reversed(s):
        if len(el) > 0:
            return len(el)
    return -1
print(last_word_len("   fly me   to   the moon  "))
