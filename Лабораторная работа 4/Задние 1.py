# TODO решите задачу
import json
def task() -> float:
    with open('input.json') as f:
      data = json.load(f)
    sum = 0

    for elem in data:
        sum += elem['score']* elem['weight']
    return round(sum,3)
    print(f'{sum:.3f}')


print(task())
