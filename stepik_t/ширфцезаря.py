n, s = int(input()), input()

for i in s:
    char = ord(chr(ord(i) - n))
    if char < 97:
        char = ord(chr(ord(i) - n + 26))
    print(chr(char), end='')
