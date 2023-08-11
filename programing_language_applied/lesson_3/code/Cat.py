#!/usr/bin/python
#-*- coding: utf-8 -*-

from code.Mammal import Mammal

class Cat(Mammal):
    def __init__(self, age, height, weight, position, fur, breed, tail_fur):
        Mammal.__init__(self, age, height, weight, position, fur)
        self.breed = breed
        self.tail_fur = tail_fur

    def tail_type(self):
        pass
    
    # since this class is child of an abstract class, we must implement all
    # abstract methods

    def move_x(self):
        print('This cat is moving on x axis')


    def move_y(self):
        print('This cat is moving on y axis')


    def move_z(self):
        print('This cat is moving on z axis')