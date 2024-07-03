import csv

with open("AAPL.csv", "rt") as csvfile:
    data = csv.reader(csvfile)
    header = data.__next__()
    i = 0
    with open("outputTask7.csv", "wt", newline='') as csvfile2:
        writer = csv.writer(csvfile2)
        for row in data:
            print(row)
            writer.writerow(row)
            i+=1
        writer.writerow(header)
        writer.writerow([i])
print(header, i , sep = "\n")