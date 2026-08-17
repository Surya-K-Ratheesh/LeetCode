from enum import Enum

def main():
    class coin(Enum):
        one_rupee = 100
        two_rupee = 200
        five_rupee = 500
        ten_rupee = 1000

    class item:
        def __init__(self, code, name, price):
            self.code = code
            self.name = name
            self.price = price

    class inventory:
        def __init__(self):
            self._slots = {}

        def add(self, item, qty):
            self._slots[item.code] = [item, qty]

        def get_item(self, code):
            slot = self._slots.get(code)
            return slot[0] if slot and slot[1] > 0 else None

        def deduct(self, code):
            self._slots[code][1] -= 1

    class VendingMachine:
        def __init__(self, inventory):
            self.inventory = inventory
            self.balance = 0

        def insert(self, coin):
            self.balance += coin.value

        def select(self, code):
            item = self.inventory.get_item(code)

            if item is None:
                return "Sold Out or No Such Slot"

            if self.balance < item.price:
                return f"Need {item.price - self.balance} more rupees"

            self.inventory.deduct(code)
            self.balance -= item.price
            change, self.balance = self.balance, 0

            return (item, change)

if __name__ == '__main__':
    main()