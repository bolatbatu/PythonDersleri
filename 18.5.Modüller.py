import csv

with open("ornek.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)