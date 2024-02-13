# TODO импортировать необходимые молули
    # TODO считать содержимое csv файла
    # TODO Сериализовать в файл с отступами равными 4
import csv
import json

input_filename = "input.csv"
output_filename = "output.json"

def task():
    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        row = list(reader)
        
    with open(output_filename, 'w') as jsonfile:
        json.dump(row, jsonfile, indent=4)


if __name__ == '__main__':

task()

with open(output_filename) as output_f:
    for line in output_f:
        print(line, end="")
