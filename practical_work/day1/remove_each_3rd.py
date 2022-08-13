"""Remove each 3rd letter in string"""

str_line = input("Input a text: ")
line = ""
for i in range(len(str_line)):
    if (i+1) % 3 == 0:
        continue
    line += str_line[i]
print(line)
