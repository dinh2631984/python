# Defining Function
"""
def add(arg1, arg2):
    total = arg1 + arg2
    return total


out = add(1, 2)
print(out)
print(add(16, 9))


def adder(arg1, arg2):
    total = arg1 + arg2
    # return total
    print(total)


print(adder(10, 50))
"""

"""
# Argument
def summ(arg):
    x = 0
    for i in arg:
        x += i
    return x


out = summ([9, 11, 25])
print(out)

out = summ([9], [11, 25])
print(out)
"""

"""
# Default Argument
def greetings(msg="Evening"):
    print(f"Good {msg}")
    print("Wellcome to the function.")


greetings("Morning")
greetings()
"""

"""
#Keyword Arguments
"""
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


vac_feedback("NMS", 85)
# vac_feedback(85, "NMS")  # Error
vac_feedback(efficacy=90, vac="Test")  # Keywords arguments
