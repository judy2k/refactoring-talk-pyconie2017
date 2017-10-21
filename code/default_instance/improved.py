from support import Config


class App(object):
    def __init__(self, path):
        self.config = None
        if path is not None:
            self._load_config(path)

    def _load_config(self, path):
        self.config = Config(path)

    def do_the_thing(self):
        print(
            "Doing the thing with "
            "config from:",
            self.config.path)

default = App(None)
load_config = default._load_config
do_the_thing = default.do_the_thing