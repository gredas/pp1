import json

with open("data (1).json") as file:
    data = json.load(file)
for x in data:
    for k,v in x.items():
        print(k,v)
print(data[0])