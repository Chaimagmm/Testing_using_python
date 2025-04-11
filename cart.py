class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item: str, quantity: int) -> None:
        """Add items to the cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items[item] = self.items.get(item, 0) + quantity

    def remove_item(self, item: str, quantity: int) -> None:
        """Remove items from the cart."""
        if item not in self.items:
            raise KeyError("Item not in cart")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items[item] -= quantity
        if self.items[item] <= 0:
            del self.items[item]

    def get_total_items(self) -> int:
        """Return total number of items in cart."""
        return sum(self.items.values())