#!/usr/bin/python3
import os
path = "/usr/bin/date"
if os.path.isfile(path):
    print(f"{path} is a file")
elif os.path.isdir(path):
    print(f"{path} is a directory")
else:
    print("Does not exist")

os.system('ls -la')
