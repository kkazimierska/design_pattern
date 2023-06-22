
def my_sum(a,b):
    return a + b

def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))

# Tuple vs List

my_tuple = (1, 2, 3)
my_tuple[0] = 9
print(my_tuple)

my_list = [1, 2, 3]
my_list[0] = 9
print(my_list)

def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

def get_kwargs(**key_value):
    a = key_value.get('a')
    b = key_value.get('b')
    return a + b