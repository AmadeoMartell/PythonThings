import csv
with open("outputTask8.csv", "wt", newline='') as csvfile:
    writer = csv.writer(csvfile)
    print("Input your data in format(Rollno,Name,Class): ")
    writer.writerow(["Rollno","Name","Class"])
    while((a:=input()) != ""): writer.writerow(a.split(","))