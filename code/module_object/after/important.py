import time

import sys

class ImportantFakeModule(object):
    @property
    def salt(self):
        return time.time()

sys.modules[__name__] = ImportantFakeModule()