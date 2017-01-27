# Feistel network

LENGTH = 6
N = 179
K = 1


def read(filename):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

    lines = [line.strip().rjust(LENGTH, '0')[:LENGTH] for line in lines]
    return [map(int, line) for line in lines]


def write(filename, blocks):
    with open(filename, 'w') as output_file:
        output_file.write('\n'.join([''.join(
            ''.join(map(str, block))
        ) for block in blocks]))


def f(k, l):
    k %= LENGTH
    return l[k:] + l[:k]


def get_next_k(k):
    return k + 1


def encrypt(blocks):
    encrypted_blocks = []
    for block in blocks:
        k = K
        l, r = block[:LENGTH / 2], block[LENGTH / 2:]
        # print 'old:', l, r
        for _ in xrange(N):
            l, r = [x ^ y for x, y in zip(f(k, l), r)], l
            k = get_next_k(k)
        encrypted_blocks.append(l + r)
        # print 'new:', l, r
    return encrypted_blocks


def get_previous_k(k):
    return k - 1


def decrypt(blocks):
    decrypted_blocks = []
    for block in blocks:
        k = N + 1
        l, r = block[:LENGTH / 2], block[LENGTH / 2:]
        # print 'new:', l, r
        for _ in xrange(N):
            k = get_previous_k(k)
            l, r = r, [x ^ y for x, y in zip(f(k, r), l)]
        decrypted_blocks.append(l + r)
        # print 'newest:', l, r
    return decrypted_blocks


if __name__ == '__main__':
    blocks = read('3.txt')
    blocks = encrypt(blocks)
    write('3_encrypted.txt', blocks)
    blocks = decrypt(blocks)
    write('3_decrypted.txt', blocks)
