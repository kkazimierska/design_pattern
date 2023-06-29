#tutaj napiszemy rozwiązanie

#Task: Import class person, define the instance and verfiy if the instance contains the attribute surname.

from has_attr import Person

#help(Person)
person2 = Person()

person2.przedstawsie()
print("Person's surname", hasattr(person2, "surname"))

def test_if_attr_surname_exist():
    assert hasattr(person2, "surname") == False


        
