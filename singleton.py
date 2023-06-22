
class Singleton(object):

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            # Instantiate the Singleton class using object = super.
            # orig = super()
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
    # why class has attribute instance?

class Settings(Singleton):
    # why we could not do it without inhertied class? Problem description.
    mode = 'dark'


s1_unique_instance = Settings()
s2_unique_instance = Settings()

print(s1_unique_instance.mode)
print(s2_unique_instance.mode)
s2_unique_instance.mode = 'light'

print(s1_unique_instance.mode)
print(s2_unique_instance.mode)

# What would happen without the Singleton design pattern?


# Whe we need Singleton pattern?
# Usage: Is it to mimic the database like behavoiur.