import json

with open('playerfile2.json','r') as f:
    data = json.load(f)

print(data)