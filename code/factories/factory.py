class ConfigObject(object):
    def __init__(self, path):
        # Read config in from path here
        pass

CONFIG_OBJECT_CACHE = {}

def Config(path):
    if path in CONFIG_OBJECT_CACHE:
        return CONFIG_OBJECT_CACHE[path]
    else:
        return CONFIG_OBJECT_CACHE.setdefault(
                path, ConfigObject(path))

config_a = Config("a.txt")
config_a2 = Config("a.txt")

print(id(config_a))
print(id(config_a2))