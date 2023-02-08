from fabric.api import *
def greeting(msg):
    print("Good %s" % msg)

def system_info():
    print("Disk Space")
    local("df -h")

    print("Ram Information")
    local("free -h")

    print("Uptime")
    local("uptime")
