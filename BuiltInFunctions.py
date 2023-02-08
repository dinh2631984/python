# w3schools
# String build in methods/functions

message = "nms jsc."
print(message)
print(message.capitalize())
print(message.upper())
print(message.isdigit())
print(message.islower())
print(message.isalpha())
print(message.find("s", 3, 6))
"""
# dir() function  in các chức năng tích hợp sẵn
print(dir(message))
print(dir([]))
print(dir({}))
print(dir(()))
"""

"""
# tuple
seq1 = ("192", "196", "198", "1008")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))
"""

"""
# Lists
mountains = ["Everest", "Himalaya", "Alps"]
print(mountains)
mountains.extend(["Mt Rainer", "Satpuda"])
print(mountains)

mountains.insert(2, "MT Abu")  # Insert them vào index thứ 2
print(mountains)

mountains.pop()  # Remove last index
# mountains.pop()
print(mountains)
mountains.pop(3)  # Remove  index 3
print(mountains)
"""

"""
# Dictionary
cntr_emp1 = {"Name": "Quốc Dĩnh", "Skill": "AI", "Code": 1024}
print(cntr_emp1)
print(cntr_emp1.keys())
print(cntr_emp1.values())
cntr_emp1.popitem()
print(cntr_emp1)
cntr_emp1.clear()
print(cntr_emp1)
"""
