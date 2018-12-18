import os

BASE_PATH = "static/mock"


for a, b, c in os.walk(BASE_PATH):
    print(a)
    print(b)
    print(c)

