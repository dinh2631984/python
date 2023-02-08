import random


def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccine is having {efficacy}% efficacy")
    if 50 < efficacy <= 75:
        print("Seem not so effective, Needs more trial")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine")
    elif efficacy >= 90:
        print("Sure, will take the shot")
    else:
        print("Need more many trials")


def order_food(min_order, *args):  # *test
    print(f"You have ordered: {min_order}")
    # print(args)
    for item in args:  # test
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 mins")
    print("Enjoy the party")


def time_activity(*args, **kwargs):
    print(args)
    print(kwargs)
    min2 = sum(args) + random.randint(0, 60)
    print(min2)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You have to spend {min2} minutes for {kwargs[choice]}")
