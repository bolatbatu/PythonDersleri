import csv

with open("20.4.data.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
