import os

print(len([1 for f in os.listdir("./") if ".py" in f and f != "main.py"]))