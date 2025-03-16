import simpy

restaurant_env = simpy.Environment()

def cook(env):
    while True:

        print('Cooking Order at %d' % env.now)

        parking_duration = 5

        yield env.timeout(parking_duration)


        print('Getting Order at %d' % env.now)

        trip_duration = 2

        yield env.timeout(trip_duration)

restaurant_env.process(cook(restaurant_env))
restaurant_env.run(until=15)
