import time

class EncryptionParameters:
    @property
    def salt(self):
        return time.time()