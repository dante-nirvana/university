# >>> Importing packages and modules <<<

import code.Cat # importing the module CAT from package CODE


new_cat = code.Cat.Cat(age=10, height=30, weight=4.5, position=(0, 0), fur= 'long',
                        breed='orange',  tail_fur='short')
new_cat.move_x()


# from code.Cat import Cat # importing only the class


# new_cat: Cat = Cat(age=10, height=30, weight=4.5, position=(0, 0), fur= 'long',
#                     breed='orange',  tail_fur='short')
# new_cat.move_x()

# _____________________________________________________________________________________#


# # >>> Design Patterns (part 1) - Creational Patterns <<<
# -------------------------------------------------------------------------------------#

# # Using Design Pattern Factory

# from code.AnimalFactory import AnimalFactory


# new_dog = AnimalFactory.new_animal(animal_type='dog', age=4, height=35, weight=19.5)
# new_cat = AnimalFactory.new_animal(animal_type='cat', age=8, height=22, weight=3.8)

# print(new_dog.position)
# print(new_cat.position)

# -------------------------------------------------------------------------------------#

# # Using Design Pattern Builder

# # Building objects without the Builder Pattern
# from code.HouseBuilder import House


# # Building a House with garage and garden
# new_house: House = House(number_bedrooms=3, number_bathrooms=2,\
#                                        has_garage=True, has_garden=True)
# print('House features:\n', new_house)

# # Building another House, without garage and with 4 bedrooms
# another_house: House = House(number_bedrooms=4, number_bathrooms=2,\
#                                             has_garden=True)
# print("Another house's features:\n", another_house)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

# # Now using the Builder Pattern
# from code.HouseBuilder import House, HouseBuilder


# # Building a House with garage and garden
# house_builder: HouseBuilder = HouseBuilder()
# new_house: House = house_builder.set_number_bedrooms(3)\
#                                 .set_number_bathrooms(2)\
#                                 .add_garage()\
#                                 .add_garden()\
#                                 .get_house()
# print('House features:\n', new_house, sep='')

# # Building a House without garage and 4 bedrooms
# another_house: House = HouseBuilder()\
#                         .set_number_bedrooms(4)\
#                         .set_number_bathrooms(2)\
#                         .add_garden()\
#                         .get_house()
# print("\nAnother house's features:\n", another_house, sep='')
