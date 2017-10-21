import codecs

import important

def encrypt(value):
    return codecs.encode(
        value + str(important.salt), 'rot13')

print(encrypt("This is totally safe."))
# Guvf vf gbgnyyl fnsr.1499173472.860092
# Guvf vf gbgnyyl fnsr.1499173473.764976