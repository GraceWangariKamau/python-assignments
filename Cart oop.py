class ShoppingCart:

    def __init__(self):
        self.items = []
        
    def add_items(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_items(self, item_name: str): 
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
        
    def calculate_total(self) -> float:
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price  # Multiply qty by price
        return total
    
    def summary(self):
        print("Cart Contents:")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ {price:.2f} each")
        print(f"Total: Ksh {self.calculate_total():.2f}\n")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_items("Kiwi", 50, 79.2)
    cart.add_items("Papaya", 30, 40.3)
    cart.add_items("Oranges", 50, 20.5)

    print(">>> Regular Cart <<<")
    cart.summary()
