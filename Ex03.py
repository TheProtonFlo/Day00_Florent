def reverseWriteAlphabet():
    x = ord('z')
    y = chr(x)

    i = 0

    while i <= 25:
        print(chr(x))
        x -= 1
        i += 1

reverseWriteAlphabet()