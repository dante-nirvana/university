from code.Dog import Dog
from code.Cat import Cat


class AnimalFactory():

    @staticmethod
    def new_animal(animal_type: str, age: int, height: float, weight: float):
        match animal_type.upper():
            case 'DOG':
                return  Dog(
                            age=age,\
                            height=height,\
                            weight=weight,\
                            position=(0, 0),\
                            fur='short',\
                            breed=None)
            
            case 'CAT':
                return Cat(
                            age=age,\
                            height=height,\
                            weight=weight,\
                            position=(0, 0),\
                            fur=None,\
                            breed=None,\
                            tail_fur=None)

