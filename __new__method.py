class Person:
    def __init__(self, name):
        self.name = name

person = Person('Kamila')

class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"The person name is {self.name}."

# Why it does not work?
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.__name__}."

instance_person = object.__new__(Person, 'Maria')
print(instance_person.__dict__)
instance_person.__init__('Maria')
print(instance_person.__dict__)




class Person:
    def __new__(cls, name):
        print(f'Creating a new {cls.__name__} object...')
        obj = object.__new__(cls)
        return obj

    def __init__(self, name):
        print(f'Initializing the person object...')
        self.name = name


person = Person('John')

