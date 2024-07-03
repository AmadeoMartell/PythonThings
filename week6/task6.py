import os
import csv
class Employee:
    def __init__(self, name='', departament="", id = 0, job_title=''):
        self.name = name
        self.id = id
        self.job_title = job_title
        self.departament = departament
    def set_name(self, name):
        self.name = name
    def set_id(self, id):
        self.id = id
    def set_job_title(self, job_title):
        self.job_title = str(job_title)
    def set_departament(self, departament):
        self.departament = departament
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_job_title(self):
        return self.job_title
    def get_departament(self):
        return self.departament
    def __str__(self):
        return f'\nДАННЫЕ СОТРУНДНИКА №{self.id}\nФИО: {self.name}\nДепартамент: {self.departament}\nДолжность: {self.job_title}\n'


def main():
    employees = {}
    if not os.path.exists('employee_list.csv'):
        f = open('employee_list.csv', "wt", newline="")
        f.close()
    with open('employee_list.csv', "rt", newline= "") as employee_list:
        reader = csv.reader(employee_list)
        for row in reader:
            employees[int(row[0])] = Employee(row[2], row[1], int(row[0]), row[3])
        while(True):
            print("Choose options: ")
            print("1. Look up an employee in the dictionary")
            print("2. Add a new employee to the dictionary")
            print("3. Change an existing employee’s name, department, and job title in the dictionary")
            print("4. Delete an employee from the dictionary")
            print("5. Save and Quit")

            match(int(input("Enter your choice num: "))):
                case 1:
                    if employees:
                        print("Choose employee id: ", ", ".join(str(x) for x in employees.keys()))
                        print(employees[int(input("Input: "))])
                    else:
                        print("No employees in dictionary!")
                        continue
                case 2:
                    print("Enter a new employee data: ")
                    temp_employee = Employee(input("Enter new employee name: "), input("Enter new employee department: "), int(input("Enter new employee id: ")) ,input("Enter new employee job title: "))
                    employees[temp_employee.get_id()] = temp_employee
                    print("NEW EMPLOYEE ADDED SUCCESSFUL!")
                case 3:
                    print("Choose employee id: ", ", ".join(str(x) for x in employees.keys()))
                    x = int(input("Input: "))
                    employees[x] = Employee(input("Enter new employee name: "), input("Enter new employee department: "), x ,input("Enter new employee job title: "))
                    print(f"EMPLOYEE №{x} CHANGED SUCCESSFUL!")
                case 4:
                    print("Choose employee id: ", ", ".join(str(x) for x in employees.keys()))
                    x = int(input("Input: "))
                    employees.pop(x)
                case 5: break
    with open('employee_list.csv', "wt", newline="") as employee_list:
        writer = csv.writer(employee_list)
        for ind in employees.keys():
            writer.writerow([employees[ind].get_id(), employees[ind].get_departament(), employees[ind].get_name(), employees[ind].get_job_title()])



if __name__ == '__main__':
    main()