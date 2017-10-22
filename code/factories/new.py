class Config(object):
    cache = {}

    def __new__(cls, path):
        if path in cls.cache:
            return cls.cache[path]
        else:
            return cls.cache.setdefault(
                path,
                super().__new__(cls))

    def __init__(self, path):
        # Read config in from path here
        print("init")


config_a = Config("a.txt")
config_a2 = Config("a.txt")

print(id(config_a))
print(id(config_a2))
