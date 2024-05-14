def writeAlphabet():
    x = ord('a')
    y = chr(x)

    i = 0

    while i <= 25:
        print(chr(x))
        x += 1
        i += 1

writeAlphabet()