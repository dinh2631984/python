# Arithmetic
x = 2
y = 5
total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = x / y
print(total)

total = y % x
print(total)

total = y ** x
print(total)

# comparision Operators
a = 30
b = 60

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a <= b)
print(out)

out = (a >= b)
print(out)

# Assignment Operators
c = 8
d = 1
c += d  # c = c + d
c -= d  # c = c - d
# print(c)

# Logical Operators

a = 40
b = 60

x = 2
y = 3

out = (a <= b) and (x >= y)
print(out)

out = (a <= b) or (x >= y)
print(out)

out = not ((a <= b) or (x >= y))
print(out)

# Membership Operator
print('****** Membership ******')
first_tuple = ("Linux", "Vagrant", "Bash", "AWS", "Ansible")
ans = "Linux" in first_tuple
print(ans)

ans = "Linux" not in first_tuple
print(ans)

# Identity Operators
print('****** Identity ******')
a = 12
b = 15
result = a is b
print(result)

result = a is not b
print(result)

