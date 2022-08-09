"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""

def strStr(haystack: str, needle: str):
    if len(needle) == 0:
        return 0
    if len(haystack.split(needle)) != 1:
        return len(haystack.split(needle))
    return -1
print(strStr("aaaaa", ""))
