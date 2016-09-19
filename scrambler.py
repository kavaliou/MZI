from sys import argv


def to_bin(text):
    for c in text:
        char_in_bin = bin(ord(c))[2:]
        for i in char_in_bin.rjust(7, '0'):
            yield int(i)


def from_bin(array):
    return chr(int(''.join(map(str, array)), 2))


def crypt(key, text):
    key = map(int, key)
    crypted_line = []
    for num, i in enumerate(to_bin(text)):
        crypted_line.append(i ^ key[0])
        if num % 7 == 6:
            s = from_bin(crypted_line)
            yield s
            crypted_line = []
        key = key[1:] + [key[0] ^ key[1] ^ key[-1]]


if __name__ == '__main__':
    key = '11001'
    if len(argv) > 2:
        key = argv[2]
    s = ''.join(crypt(key, argv[1]))
    s1 = ''.join(crypt(key, s))
    print s
    print s1
