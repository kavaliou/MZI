# Scramblers
KEY = '11001'


def read(filename):
    with open(filename, 'r') as input_file:
        return input_file.readline().strip()


def write(filename, line):
    with open(filename, 'w') as output_file:
        output_file.write(line)


def crypt(line):
    key = map(int, KEY)
    crypted_line = []
    for index in xrange(0, len(line), 5):
        block = map(int, line[index:index+len(key)])
        crypted_block = [str(x ^ y) for x, y in zip(key, block)]
        crypted_line.append(''.join(crypted_block))
        key = [key[0] ^ key[1] ^ key[-1]] + key[1:]
    return ''.join(crypted_line)


if __name__ == '__main__':
    line = read('2.txt')
    line = crypt(line)
    write('2_encrypted.txt', line)
    line = crypt(line)
    write('2_decrypted.txt', line)
