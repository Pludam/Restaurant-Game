import simpy

restaurant_env = simpy.Environment()
order_store = simpy.Store(restaurant_env,10)
order_inter = 7


def add_order(env: simpy.Environment, order_store: simpy.Store):
    order_i = 0
    while True:
        order_i +=1
        yield env.timeout(order_inter)
        print(f"adding Order: {order_i} at {env.now}")
        order_store.put(f"Order: {order_i}")

    

def cook(env: simpy.Environment,order_store: simpy.Store):
    while True:
        
        print('requesting Order at', env.now)

        item = yield order_store.get()

        
        print(f'Cooking {item} at {env.now}')

        cook_duration = 5

        yield env.timeout(cook_duration)

restaurant_env.process(add_order(restaurant_env,order_store))
restaurant_env.process(cook(restaurant_env,order_store))

restaurant_env.run(until=15)
