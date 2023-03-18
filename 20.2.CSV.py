import csv

with open("20.3.data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["ad"],row["soyad"],row["yaş"])