from support import Config


class App(object):
    def __init__(self):
        self.config = None

    def load_config(self, path):
        self.config = Config(path)

    def do_the_thing(self):
        print(
            "Doing the thing with config from:",
            self.config.path)

default = App()
load_config = default.load_config
do_the_thing = default.do_the_thing