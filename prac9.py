import csv
import json

with open('test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

with open('test.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data has been converted to JSON successfully")