#!/usr/bin/env python3

import pytest
from lib.shoe import Shoe

def test_shoe_creation():
    shoe = Shoe("Nike", 10)
    assert shoe.brand == "Nike"
    assert shoe.size == 10
    assert shoe.is_sold is False

def test_sell_shoe():
    shoe = Shoe("Nike", 10)
    shoe.sell()
    assert shoe.is_sold is True

def test_return_shoe():
    shoe = Shoe("Nike", 10)
    shoe.sell()
    shoe.return_shoe()
    assert shoe.is_sold is False

        
        
   
