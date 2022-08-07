"""Make the first letters capital"""

import urllib.request

get_url = urllib.request.urlopen('https://projecteuler.net/project/resources/p022_names.txt')

for line in get_url:
    output = line.title()

    # This will print the output
    with open('text.txt', 'w') as f:
        f.write(str(output))
