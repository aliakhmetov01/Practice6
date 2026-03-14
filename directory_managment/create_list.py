from pathlib import Path
import os

father_dir = Path("father")

children_dir = [
    "child-1",
    "child-2",
    "child-3"
]

print(f"current direction: {os.getcwd()}")

for folder in children_dir:
    path = father_dir / folder
    os.makedirs(path, exist_ok = True)
print("dir created!")