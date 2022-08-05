"""Make the first letters capital in the text"""

with open('file2.txt', 'r') as file2, open('file2_new.txt', 'a') as file2_new:
    open('file2_new.txt', 'w').close()
    for line in file2:
        file2_new.write(line.title())
