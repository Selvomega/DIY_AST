tab = "    "

with open("test_input.py",'r') as handle:
    data = handle.read().replace(tab,"hhhh")
print(data)
