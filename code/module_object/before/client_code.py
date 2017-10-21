import codecs

import important

def encrypt(value):
    return codecs.encode(
        value + str(important.salt), 'rot13')

print(encrypt("This is totally safe."))
