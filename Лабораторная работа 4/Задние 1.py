# TODO решите задачу
import json
def task(filename):
    with open(filename) as json_file:
      data = json.load(json_file)
    
    sum = sum([value["score"] * value["weight"] for value in data])
    return round(sum, 3)
    
result = task("input.json")

print(result)
