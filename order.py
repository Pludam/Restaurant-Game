from enum import Enum

class OrderStatus(Enum):
    RECIEVED = 1
    COOKING = 2
    FINNISHED = 2

class Order:
    _id = 0

    def __init__(self,name: str,quantity: int, status: OrderStatus):
        Order._id += 1
        self.id = Order._id
        self.name = name
        self.quantity = quantity
        self.status = status

        