# __new__ method
# https://www.pythontutorial.net/python-oop/python-__new__/

class Person:
    def __init__(self, name):
        self.name = name

person = Person('Kamila')


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

# super call

class Person:
    def __new__(cls, first_name, last_name):
        # create a new object
        obj = super().__new__(cls)

        # initialize attributes
        obj.first_name = first_name
        obj.last_name = last_name

        # inject new attribute
        obj.full_name = f'{first_name} {last_name}'
        return obj


person = Person('John', 'Doe')
print(person.full_name)

print(person.__dict__)