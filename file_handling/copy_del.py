import os

if os.path.exists("temp.txt"):
    os.remove("temp.txt")
else: print("File doesn't exist")