import simpy
from order import Order
import random

restaurant_env = simpy.Environment()
order_store = simpy.Store(restaurant_env,10)
order_inter = 7
order_type = ["fries", "burger","soda"]
cook_time = {"fries":5,"burger":6, "soda":3 }
order_quantity_min, order_quantity_max = 1,5


def add_order(env: simpy.Environment, order_store: simpy.Store):
    while True:
        yield env.timeout(order_inter)
        order_quantity = random.randint(order_quantity_min,order_quantity_max)
        order = Order(random.choice(order_type),order_quantity)
        #print(f"adding Order[{order.id}]: {order.name} with quantity {order_quantity} at {env.now}")
        order_store.put(order)

    

def cook(env: simpy.Environment,order_store: simpy.Store):
    while True:
        
        print('waiting for Order at', env.now)

        order: Order = yield order_store.get()

        for i in range(order.quantity):
            i += 1
            print(f'Cooking Order {order.name} {i} of {order.quantity}, ID {order.id} at {env.now}')
            yield env.timeout(cook_time[order.name])
        print(f"finnished Cooking at {env.now}")

restaurant_env.process(add_order(restaurant_env,order_store))
restaurant_env.process(cook(restaurant_env,order_store))

restaurant_env.run(until=1000)
