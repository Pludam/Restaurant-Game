from order import Order

class Customer():
    _id = 0
    def __init__(self,order: Order):
        Customer._id += 1
        self.id = Customer._id
        self.order = order
        self.table = "" # unused