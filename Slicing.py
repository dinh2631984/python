planet1 = "Closest of Sun"
print(planet1)
print(planet1[0])
print(planet1[1])
print(planet1[2])

print(planet1[-1])
print(planet1[-2])

# Slicing a tring, get a substring from a string
print(planet1[0:3])  # From Pos1 to Pos2
print(planet1[:])
print(planet1[:6])
print(planet1[9:])

# Slicing Tuple
devops = ("Linux", "Vagrant", "Bash", "AWS", "Ansible")
print(devops[0])
print(devops[4])
print(devops[-2])
print(devops[2:4])
print(devops[-2:4])
print(devops[2:4][1])
print(devops[2:4][1][2])
print(devops[2:4][1][1:])

# Dictionary Example
Skills = {"devops": ("Linux", "Vagrant", "Bash", "AWS", "Ansible"),
          "development": ("Java", "PHP", "NodeJS"),
          "Operation": ("Linux", "Windows", "CMD")}
print(Skills)
print(Skills["development"])
print(Skills["development"][1:3])

planet1 = "Closest of Sun"
print(planet1[2:5])
