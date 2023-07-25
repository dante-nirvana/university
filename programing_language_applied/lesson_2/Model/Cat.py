#!/usr/bin/python
#-*- coding: utf-8 -*-

from Mammal import Mammal

class Cat(Mammal):
    def __init__(self, age, height, weight, position, fur, breed, tail_fur):
        Mammal.__init__(self, age, height, weight, position, fur)
        self.breed = breed
        self.tail_fur = tail_fur

    def tail_type(self):
        pass

