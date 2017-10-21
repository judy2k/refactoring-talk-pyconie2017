from support import Config

config = None

def load_config(path):
    global config
    config = Config(path)

def do_the_thing():
    print(
        "Doing the thing with config from:",
        config.path)