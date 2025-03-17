
class Order:
    _index = 0

    def __init__(self,name: str,quantity: int):
        self.id =Order._index + 1
        self.name = name
        self.quantity = quantity

        Order._index += 1