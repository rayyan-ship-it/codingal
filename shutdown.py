import os
def shutdown_system():
    shutdown_system=input("do u want to shut down ur system (yes/no)")
    if shutdown_system=="yes":
        print("shutdown the system")
    elif shutdown_system=="no":
        print("system shutdown cancelled")
    else:
        print("invalid input")
shutdown_system()