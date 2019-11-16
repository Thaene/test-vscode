import math

# from os import rename

# import sys

import requests

# print(sys.version)
print(sys.executable)

# name = input("Your Name?")
# print("Hello,", name)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Steve'))
r = requests.get("https://coreyms.com")
print(r.status_code)
