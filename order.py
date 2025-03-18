from enum import Enum
import simpy
class OrderStatus(Enum):
    RECIEVED = 1
    COOKING = 2
    FINNISHED = 2

class Order:
    _id = 0

    def __init__(self,env: simpy.Environment,name: str,quantity: int,):
        Order._id += 1
        self.id = Order._id
        self.name = name
        self.quantity = quantity
        self.completed_event = simpy.Event(env)

        