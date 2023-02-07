# Break and Continue Statement
"""
for i in "DevOps":

    if i == 'O':
        # print("Found my data")
        # break
        continue
    print(i)
print("Out of loop")
"""
import random

Vaccines = ["Moderna", "Pfizer", "vn", "eu"]
random.shuffle(Vaccines)
print(Vaccines)
Lucky = random.choice(Vaccines)
print(Lucky)

for vac in Vaccines:
    print(f"***Testing Vaccine {vac}***")
    if vac == Lucky:
        print(f"{Lucky} Vaccine, Test Successfully")
        print()
        break
    print("Failed")
