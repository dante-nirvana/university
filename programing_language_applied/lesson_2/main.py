# OBJECT ORIENTED PROGRAMING AND UML DIAGRAM

# This module will approach the following topics:

# * use of classes and "constructor" (__init__ method) in Python
# * how to instatiate an object in the main program
# * the use of "self" word
# * class attributes vs object attributes
# * special attributes, like __class__ and __name__

# # 1 - Class implementation

class Dog: # this line creates a class named 'Dog'
    def __init__(self) -> None: # this line redefines the special method __init__()
    # which is a initializer for the class
# Note: "-> Type" is the notation on python to indicate the data type returned by a
# method. This practice is called 'Type Hinting'.
# Note2: 'self' is a reference to the very object (instance) that we are manipulating
# in the moment
        pass

# by default, python recognizes any code outside the body of classes and functions
# as it is inside the kickstart function, usually called main function on strongly
# typed languages

# --- " main " ---
rex: Dog = Dog() # this line instantiates a new object of 'Dog' class
print(rex)


# # 2 - Attributes inside the __intt__()

# class Dog:
#     def __init__(self) -> None:
#         self.age = 5 # attribute already initialized inside the __init__()


# rex: Dog = Dog()
# caramel: Dog = Dog()
# print(f"Rex's age is: {rex.age}")
# print(f"Caramel's age is: {caramel.age}")

# Note: if used this way, every instance will have same values for their attributes


# # 3 - Initializing attributes with parameters

# class Dog:
#     def __init__(self, age) -> None:
#         self.age = age # note that 'self.age' is the attribute and 'age'
#         # is the parameter passed as the value for the for the actual age
#         # of the instance


# rex: Dog = Dog(4) # here a value is passed for the initializer, and then 
# # this value will be passad to the attribute 'self.age', which means
# # that rex is now 4 years old
# caramel: Dog = Dog(6) # and caramel is 6
# print(f"Rex's age is: {rex.age}")
# print(f"Caramel's age is: {caramel.age}")


# # 4 - Class global attributes

# class Dog:
#     family = 'Canidae'

#     def __init__(self, age) -> None:
#         self.age = age


# rex: Dog = Dog(4)
# caramel: Dog = Dog(6)
# print(f"Rex's age is: {rex.age}; Rex is a dog, dogs's family is: {rex.family}")
# print(f"Caramel's age is: {rex.age}; Caramel is a dog, dogs's family is: {rex.family}")
# # and we can also access classes's global attributes (since they're not protected)
# print(f"All dogs belong to the '{Dog.family}' family")


# # 5 - Type hinting and special attributes __class__ and __name__

# class Dog:
#     family: str = 'Canidae'

#     def __init__(self, name: str, age: int):
#         self.name: str = name
#         self.age: int = age
# # Note: type hinting is a good practice and helps if we need to refactor the code later.
# # It also allows us to use any attribute or methods# from the type we gave for our/
# #                                                                            variables

# rex: Dog = Dog('Rex', 5)
# caramel: Dog = Dog('Caramel', 8)

# # Now we can verify our instances using their attribute 'name'
# print(f"What's the class that {rex.name} is from? R: {rex.__class__.__name__}")
# print(f"What's the class that {caramel.name} is from? R: {caramel.__class__.__name__}")
# # Note: object.__class__.__name__ is the same thing that Class.__name__, but since
# # we may not know what class an object is from, than  we need to use __class__


# # 6 - Protected attributes

# class Dog:
#     family: str = 'Canidae'

#     def __init__(self, name: str, age: int, weight: float):
#         self.name: str = name
#         self._age: int = age
#         self._weight: float = weight
#         # self.__weight: float = weight # exemple of protected attribute

# # Note:
# # the double underscore before AND after a members name is reserved to special methods,
# # called 'Magic' or 'Dunder' Methods. One underscore before the name of a variable or
# # method means the member is "protected" (almost) and should not be changed in the class
# # And if there is double underscore ONLY before, that means this member is fully
# # protected and an AttributeError exception you be raised if we try to manipulate it
# # outside the class.

# rex: Dog = Dog('Rex', 5, 23.5)
# caramel: Dog = Dog('Caramel', 7, 13.5)

# print(f"Rex's age: {rex._age}, Rex's weight: {rex._weight}")
# print(f"Caramels's age: {caramel._age}, Rex's weight: {caramel._weight}")

# # test with protected attribute
# # print(f"Rex's age: {rex._age}, Rex's weight: {rex.__weight}")
# # print(f"Caramels's age: {caramel._age}, Rex's weight: {caramel.__weight}")


# # 7 - Accessing protected attributes with methods
# class Dog:
#     family: str = 'Canidae'

#     def __init__(self, name: str = 'doggie doe', age: int = 0, weight: float = 0):
#         self.__name: str = name
#         self.__age: int = age
#         self.__weight: float = weight

#     # the methods bellow allow us to access protected attributes
#     def get_name(self): return self.__name
#     def set_name(self, name: str): self.__name = name

#     def get_age(self): return self.__age
#     def set_age(self, age: int): self.__age = age

#     def get_weight(self): return self.__weight
#     def set_weight(self, weight: float): self.__weight = weight

# # Note: the names 'get' and 'set' are conventions, and methods that get and set values
# # are called 'getters' and 'setters'

# rex: Dog = Dog('Rex')
# caramel: Dog = Dog(age=2, weight=33.5)

# rex.set_age(8)
# rex.set_weight(13.25)
# caramel.set_name('Caramel')

# print(f"Dog name: {rex.get_name()}; age: {rex.get_age()}; weight: {rex.get_weight()}")
# print(f"Dog name: {caramel.get_name()}; age: {caramel.get_age()}; weight: {caramel.get_weight()}")

# # Note: using getters and setter the progrom will not raise AttributeError, but there is
# # a more "pythonic" way of protecting attributes.


# 8 - Inheritance

# class Animal:
#     x, y, z = 0, 1, 2

#     def __init__(self, age: int, height: int, weight: float, position: tuple):
#         self.age: int = age
#         self.height: int = height
#         self.weight: float = weight
#         self.position: tuple = position # for movements on x, y, z axis =)

#         def move_x(self): self.position[self.x] += 1

#         def move_y(self): self.position[self.y] += 1

#         def move_z(self): self.position[self.z] += 1


# class Dog(Animal): # Dog inherits from Animal
#     def __init__(self, age: int, height: int, weight: float, position: tuple):
#         Animal.__init__(self, age, height, weight, position)
#     # this notation is easier and do the exact same as above, but can only be used
#     # by chield classes
    
#     def move_z(self): self.position[super().z] += 2


# caramel: Dog = Dog(2, 60, 43.5, (0, 0, 0))
# print(caramel.age)
