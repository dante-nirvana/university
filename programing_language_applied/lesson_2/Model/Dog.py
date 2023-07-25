#!/usr/bin/python
#-*- coding: utf-8 -*-

from Mammal import Mammal

class Dog(Mammal):
    def __init__(self, age, height, weight, position, fur, breed):
        Mammal.__init__(self, age, height, weight, position, fur)
        self.breed = breed

