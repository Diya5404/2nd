# from os import write
#
# with open('stock_data.csv','r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             print(row)
import csv

with open("output.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['name','age','city'])
    writer.writerow(['diya',21,'kannur'])
    writer.writerow(['John',22, 'kasargod'])

with open("dictoutput.csv",'w') as file:
    fieldnames = ['name','age','city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Diya', 'age': 21, 'city':'kannur'})
    writer.writerow({'name': 'John', 'age':22, 'city': 'Kasargod'})

try:
     with open('stock_data.csv','r') as file:
         reader = csv.reader(file)
         for row in reader:
             print(row)

except csv.Error as e:
    print(f'Error reading CSV file: {e}')


