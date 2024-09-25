import csv

with open('dtock_data.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


