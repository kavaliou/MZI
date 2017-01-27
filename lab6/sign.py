from lab4 import rsa
from lab5 import sha256


def sign(data, private_key):
    h = sha256.sha256(data)
    return rsa.encrypt(h, private_key)


def check_sign(data, signature, public_key):
    decrypted = rsa.decrypt(signature, public_key)
    h = sha256.sha256(data)
    return h == decrypted


def test():
    public_key, private_key = rsa.generate_keys()

    data = 'Hello World'

    signature = sign(data, private_key)
    result = check_sign(data, signature, public_key)

    print 'ok' if result else 'failed'
    print 'data:\n', data
    print 'signature:\n', hex(signature)


if __name__ == '__main__':
    test()
