import csv
with open("employee_records.csv", "wt", newline='') as csvfile:
    writer = csv.writer(csvfile)
    print("Input your data in format(Name,Age,City): ")
    writer.writerow(["Name","Age","City"])
    while((a:=input()) != ""): writer.writerow(a.split(","))

num_of_column = dict(Name = 0, Age = 1, City = 2)
while(True):
    with open("employee_records.csv", "rt", newline='') as csvfile:
        reader = csv.reader(csvfile)
        i = num_of_column[input("Select a column that you want output: ")]
        for row in reader:
            print(row[i])
    print("Do you want to continue? (y/n): ")
    if input() == "y": continue
    else: break