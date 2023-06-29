class Person:
    age = 23
    name = "Adam"
    def przedstawsie(self):
        print(f"Nazywam się {self.name} i mam {self.age} lat")
    

person = Person()

#print("Person's age:", hasattr(person, "age"))
#print("Person's salary:", hasattr(person, "salary"))

# Output:
# Person's age: True
# Person's salary: False