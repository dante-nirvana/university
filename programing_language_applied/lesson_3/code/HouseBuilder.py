# Creational Design Pattern: Builder


# # Not using the Builder Pattern
class House:
    def __init__(self, num_bedrooms: int=None,num_bathrooms: int=None,\
                 has_garage: bool=False, has_garden: bool=False) -> None:
        self.num_bedrooms: int = num_bedrooms
        self.num_bathrooms: int = num_bathrooms
        self.has_garage: bool = has_garage
        self.has_garden: bool = has_garden

    
    def __str__(self) -> str:
        features: list = list()
        if self.num_bedrooms:
            features.append(f'Number of rooms: {self.num_bedrooms}')
        if self.num_bathrooms:
            features.append(f'Number of bathrooms: {self.num_bathrooms}')
        if self.has_garage:
            features.append('Has garage')
        if self.has_garden:
            features.append('Has garden')

        return ', '.join(features)

# -------------------------------------------------------------------------------------#
# _____________________________________________________________________________________#

# # Using the Builder Pattern

# class House:
#     def __init__(self) -> None:
#         self.num_bedrooms: int = None
#         self.num_bathrooms: int = None
#         self.has_garage: bool = None
#         self.has_garden: bool = None


#     def __str__(self) -> str:
#         features: list = list()
#         if self.num_bedrooms:
#             features.append(f'Number of bedrooms: {self.num_bedrooms}')
#         if self.num_bathrooms:
#             features.append(f'Number of bathrooms: {self.num_bathrooms}')
#         if self.has_garage:
#             features.append('Has garage')
#         if self.has_garden:
#             features.append('Has garden')

#         return ',\n'.join(features)
    

# class HouseBuilder:
#     def __init__(self) -> None:
#          self.house = House()


#     def set_number_bedrooms(self, num_bedrooms: int):
#         self.house.num_bedrooms = num_bedrooms
#         return self


#     def set_number_bathrooms(self, num_bathrooms: int):
#         self.house.num_bathrooms = num_bathrooms
#         return self


#     def add_garage(self):
#         self.house.has_garage = True
#         return self


#     def add_garden(self):
#         self.house.has_garden = True
#         return self


#     def get_house(self):
#         return self.house
