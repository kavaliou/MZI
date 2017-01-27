# Caesar cipher
alphabet = [unichr(i) for i in xrange(ord('a'), ord('z')+1)]


def encrypt(text, key):
    new_text = []
    for char in text:
        try:
            index = alphabet.index(char)
            new_text.append(alphabet[(index + key) % len(alphabet)])
        except:
            new_text.append(char)
    return ''.join(new_text)


def decrypt(text):
    return [encrypt(text, key) for key in xrange(len(alphabet))]


if __name__ == '__main__':
    with open('1.txt', 'r') as input_file:
        text = unicode(''.join(input_file.readlines()))
    # text = unicode('lab mzi checking the caesar cipher')
    # print encrypt(text, 13)
    for i, v in enumerate(decrypt(text)):
        print len(alphabet) - i, v
