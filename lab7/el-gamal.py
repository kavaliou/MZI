import random

from eleptic import el_mul, mod_inv


def generate_keys():
    """
    :return: public_key, private_key
    """

    p = 6277101735386680763835789423207666416083908700390324961279
    a = -3
    b = 2455155546008943817740293915197451784769108058161191238065

    Gx = 602046282375688656758213480587526111916698976636884684818
    Gy = 174050332293622031404857552280219410364023488927386650641

    n = 6277101735386680763835789423176059013767194773182842284081
    h = 1

    c = random.randint(2, p - 1)
    Dx, Dy = el_mul(c, Gx, Gy, p, a)

    return (p, a, Gx, Gy, Dx, Dy), (p, a, c)


def encrypt(data, public_key):
    p, a, Gx, Gy, Dx, Dy = public_key

    k = random.randint(2, p - 2)
    Rx, Ry = el_mul(k, Gx, Gy, p, a)
    x, _ = el_mul(k, Dx, Dy, p, a)
    e = (data * x) % p

    return Rx, Ry, e


def decrypt(data, private_key):
    p, a, c = private_key
    Rx, Ry, e = data

    x, _ = el_mul(c, Rx, Ry, p, a)
    m = (mod_inv(x, p) * e) % p

    return m


def test():
    data = 1234567890
    public_key, private_key = generate_keys()

    encrypted = encrypt(data, public_key)
    decrypted = decrypt(encrypted, private_key)

    print 'data:', data
    print 'encrypted:', encrypted
    print 'decrypted:', decrypted


if __name__ == '__main__':
    test()
