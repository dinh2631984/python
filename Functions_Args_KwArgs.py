# Variable Length Arguments   *args  (Non Keyword Arguments)
def order_food(min_order, *args):  # *test
    print(f"You have ordered: {min_order}")
    # print(args)
    for item in args:  # test
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 mins")
    print("Enjoy the party")


order_food("Salag", "Pizza", "Biryani")

# Variable Length Arguments  **kwargs  (Keyword Arguments)

import random


def time_activity(*args, **kwargs):
    print(args)
    print(kwargs)
    min2 = sum(args) + random.randint(0, 60)
    print(min2)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You have to spend {min2} minutes for {kwargs[choice]}")


time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")
