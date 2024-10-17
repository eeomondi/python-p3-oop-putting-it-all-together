#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.is_sold = False

    def sell(self):
        self.is_sold = True

    def return_shoe(self):
        self.is_sold = False
