import csv

list_of_dicts = [
    {'name': 'Masha', 'age': 25, 'job': 'scientist'},
    {'name': 'Pasha', 'age': 34, 'job': 'programmer'},
    {'name': 'Sasha', 'age': 41, 'job': 'big boss'}
    ]

with open('3_4_result.csv', 'w', encoding='utf-8', 
          newline='') as f:
          fields = ['name', 'age', 'job']
          writer = csv.DictWriter(f, fields, delimiter=';')
          writer.writeheader()
          for dict in list_of_dicts:
              writer.writerow(dict)
          
with open('3_4_result.csv', 'r', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    for dict in list_of_dicts:
        print(dict)