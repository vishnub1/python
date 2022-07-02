# A classes is a blueprint of an object

"""
 - Classes are created by keyword class
 - Attributes are the variables that belong to a class.

 syntax:
 ------
        Class ClassName:
            #statement-1
            .
            .
            .
            #statement-2
 - Attributes are always public and can be accessed using the dot(.) operator.
"""

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
print("---------------------------")

# init function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print("---------------------------")
# John
# 36


# The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age



  # Object Methods
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# The self Parameter
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()



# Modify Object Properties
p1.age = 40


# Delete Object Properties
del p1.age


# Delete Objects
del p1

# The pass Statement
class Person:
  pass
