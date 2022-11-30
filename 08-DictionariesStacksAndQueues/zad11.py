import json

with open("data.json") as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)

while i < len(data):
    for k,v in data.items():
    print(k,":",v)
    i += 1
