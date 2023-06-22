[10 design patterns explained](https://www.youtube.com/watch?v=tv-_1er1mWI)

### Design patterns
**Creational** = Singleton(1:35 - 2:25), Prototype, Builder, Factory

**Structural** = Facade, Proxy

**Behavioral** = Iterator, Observer, Mediator, State

[Refactoring - Singleton Design Pattern](https://refactoring.guru/pl/design-patterns/singleton)

### Goal
existance of only one instance class.

### Problem
- ensure existance of only one insatnce of the class,
you can not implement it using consructor, because by definition it returns new objects
- ensure access to this instance globally; globall variables have risk of overwriting it; it is better to keep all code in one class, which is contstrained to unique instance
- nothing except the class itself can not overwrite it

### Solution
- constructor should be private
- static method to create an instance, which will have a role of constructor, so the calls of the class returns existing instance

### Usage
Singleton is used if you need only one instance of the class. It could be a database connection.

### Cons
- breaks the rule of single responsibility, it solves two problems

### Implementation
1. Before getting to the [implementation of Singleton](https://stackoverflow.com/questions/42237752/single-instance-of-class-in-python) in `singleton.py`, we need to understand few concepts.

2. [Class and object in python](https://www.w3schools.com/python/python_classes.asp)

How to check the instance of the class?
Super of the self class?

3. [new method tutorial](https://www.pythontutorial.net/python-oop/python-__new__/) explains what is in the new method of the python object. Go to ``__new__ method.py`.


4. [How to pass args and kwargs?](https://realpython.com/python-kwargs-and-args/)

5. [hasattr method](# https://www.programiz.com/python-programming/methods/built-in/hasattr)

6. [Super call forward](https://www.educative.io/answers/what-is-super-in-python) and [Super call backward](https://realpython.com/python-super/).