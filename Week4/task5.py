import csv

with open("AAPL.csv", "rt") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    select = int(input("Enter column num: "))
    for row in data:
        print(row[select])