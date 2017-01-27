# RSA
from fractions import gcd
from random import choice


LAST_PRIME_NUMBER = 1000000


def binary_power(number, power, mod):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= number
            result %= mod
        number *= number
        number %= mod
        power /= 2
    return result


def get_prime_numbers():
    is_prime = [True] * LAST_PRIME_NUMBER
    prime_numbers = [2]
    for number in xrange(3, LAST_PRIME_NUMBER, 2):
        if is_prime[number]:
            prime_numbers.append(number)
            for j in xrange(number*number, LAST_PRIME_NUMBER, number):
                is_prime[j] = False
    return prime_numbers


def get_d(a, b, x, y):
    if a == 0:
        x[0] = 0
        y[0] = 1
        return b
    x1, y1 = [-100500], [-100500]
    d = get_d(b % a, a, x1, y1)
    x[0] = y1[0] - (b / a) * x1[0]
    y[0] = x1[0]
    return d


def encrypt(line, public_key):
    line = int(line, 2)
    return bin(binary_power(line, public_key[0], public_key[1]))[2:]
    # return bin(line**public_key[0] % public_key[1])[2:]


def decrypt(line, private_key):
    line = int(line, 2)
    return bin(binary_power(line, private_key[0], private_key[1]))[2:]
    # return bin(line**private_key[0] % private_key[1])[2:]


def read(filename):
    with open(filename, 'r') as input_file:
        return input_file.readline().strip()


def write(filename, text):
    with open(filename, 'w') as output_file:
        output_file.write(text)


if __name__ == '__main__':
    prime_numbers = get_prime_numbers()
    p, q = choice(prime_numbers), choice(prime_numbers)
    phi = (p - 1)*(q - 1)
    for e in xrange(3, LAST_PRIME_NUMBER, 2):
        if gcd(e, phi) == 1:
            break
    x, y = [-100500], [-100500]
    if get_d(e, phi, x, y) == -1:
        print 'very bad :('
        exit()
    d = x[0]
    if d < 0:
        d += phi
    print 'public keys:', e, p*q
    print 'private keys:', d, p*q

    text = read('7.txt')
    encrypted_text = encrypt(text, (e, p*q))
    # write('7_encrypted.txt', encrypted_text)
    decrypted_text = decrypt(encrypted_text, (d, p*q))
    # write('7_decrypted.txt', decrypted_text)
    # print encrypted_text
    # print decrypted_text
    print text == decrypted_text
