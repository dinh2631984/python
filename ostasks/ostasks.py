#!/usr/bin/python3
import os

userList = ["alpha", "beta", "gamma"]
# print(userList)
print("Adding users to system")
print("##################################################################################################")
for user in userList:
    exitcode = os.system(f"id {user}")
    if exitcode != 0:
        print("User {} does not exist. Adding user ".format(user))
        print("##################################################################################################")
        print()
        os.system(f"useradd -m {user}")
    else:
        print(f"User {user} already exist. Skipping ...")
        print("##################################################################################################")
        print()

exitcode = os.system(f"grep science /etc/group")
if exitcode != 0:
    print("Group science does not exist. Adding it ")
    print("##################################################################################################")
    print()
    os.system(f"groupadd science")
else:
    print(f"Group science already exist. Skipping ...")
    print("##################################################################################################")
    print()

for user in userList:
    print(f"Adding {user} in the science group")
    print("###############################################################################")
    print()
    os.system(f"usermod -G science {user}")

dir_path = "/tmp/ostasks"
if os.path.isdir(dir_path):
    print(f"Directory {dir_path} already exist, skipping it...")
else:
    print(f"Creating {dir_path} directory")
    os.mkdir(dir_path)

print(f"Assigning permisson and ownership to the directory {dir_path}")
print("#################################################################################")
print()
os.system(f"chown :science {dir_path}")
os.system(f"chmod 770 {dir_path}")
