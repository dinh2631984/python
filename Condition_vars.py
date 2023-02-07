DevOps = ["Ansible", "Docker", "Kubernetes", "Puppet"]
Dep = ("NodeJS", "PHP", "Java", "Python")
cntr_emp1 = {"Name": "Phan Quốc Dĩnh", "Skill": "AI", "Code": 1298}
cntr_emp2 = {"Name": "NMS", "Skill": "Blockchanin", "Code": 1989}

user_skill = input("Enter your desired skill: ")
# print(user_skill)
if user_skill in DevOps:
    print(f"We have {user_skill} in DevOps Team.")
elif (user_skill in Dep):
    print(f"We have {user_skill} in Development Team.")
elif (user_skill in cntr_emp1.values()) or (user_skill in cntr_emp2.values()):
    print("We have contract employees with this skills")
else:
    print("Skill not found")
    print("Please check if  you have entered capitalize or check the spelling")
