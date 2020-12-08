import os

for (root, directories, files) in os.walk("C:\\Users"):
    for filename in directories:
        print(filename)