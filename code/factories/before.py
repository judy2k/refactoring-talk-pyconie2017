class Config(object):
    def __init__(self, path):
        # Read config in from path here
        pass


config_a = Config("a.txt")
config_a2 = Config("a.txt")

print(id(config_a))
print(id(config_a2))