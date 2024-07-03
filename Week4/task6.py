import csv

with open("AAPL.csv", "rt") as csvfile:
    data = csv.reader(csvfile)
    select = input("Enter your data: ")
    print(data.__next__())
    for row in data:
        if select in row: print(row)