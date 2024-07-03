import csv

with open("AAPL.csv", "rt") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    for row in data:
        print(row)