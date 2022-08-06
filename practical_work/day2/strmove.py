"""Transfer the word letters in front of by size"""

def strmove(str_line, position):
    str_moved = str_line[-position:]
    rest_part = str_line[:-position]
    return str_moved + rest_part
word = input("Input a word: ")
move = int(input("Inpu the size of moving: "))
print(strmove(word, move))
