import json

filename = "metrics.json"

with open(filename, "r") as f:
    data = json.load(f)

for key in data:
    data[key] += 1

with open(filename, "w") as f:
    json.dump(data, f, indent=4)
