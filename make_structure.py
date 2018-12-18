import os

BASE_PATH = "static/mock/"

print("-" * 80)
for root, dirs, files in os.walk(BASE_PATH):
    route = root.replace(BASE_PATH, "/")
    print("root : ", route)
    print("dirs : ", dirs)
    print("files: ", files)
    print("-" * 80)




