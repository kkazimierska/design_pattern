# https://stackoverflow.com/questions/42237752/single-instance-of-class-in-python

class Singleton(object):
    # https://www.w3schools.com/python/python_classes.asp
    def __new__(cls, *args, **kw):
        # why cls, why args?
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            # what is super
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
    # why class has attribute instance?

class Settings(Singleton):
    # why we could not do it without inhertied class?

    def __init__(self):
        self.mode = 'dark'

    # Ensure only one object can be created

s1_unique_instance = Settings()
s2_unique_instance = Settings()

print(s1_unique_instance.mode)
print(s2_unique_instance.mode)
s2_unique_instance.mode = 'light'

print(s1_unique_instance.mode)
print(s2_unique_instance.mode)

# What would happen without the Singleton design pattern?


