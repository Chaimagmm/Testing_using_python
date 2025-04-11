import pytest
from cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 3)
    assert cart.get_total_items() == 3

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("banana", 5)
    cart.remove_item("banana", 2)
    assert cart.get_total_items() == 3

def test_invalid_quantity():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("orange", -1)