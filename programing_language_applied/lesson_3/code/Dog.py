#!/usr/bin/python
#-*- coding: utf-8 -*-

from code.Mammal import Mammal

class Dog(Mammal):
    def __init__(self, age, height, weight, position, fur, breed):
        Mammal.__init__(self, age, height, weight, position, fur)
        self.breed = breed

    # since this class is child of an abstract class, we must implement all
    # abstract methods

    def move_x(self):
        print('This dog is moving on x axis')


    def move_y(self):
        print('This dog is moving on y axis')


    def move_z(self):
        print('This dog is moving on z axis')
