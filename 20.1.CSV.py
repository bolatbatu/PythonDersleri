import csv

with open("20.2.data.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
