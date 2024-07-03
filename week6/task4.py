class Employee:
    def __init__(self, name='', departament="", id= "", job_title=''):
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

# Susan Meyers 47899 Accounting Vice President
# Mark Jones 39119 IT Programmer
# Joy Rogers 81774 Manufacturing Engineer
def main():
    employeers = []
    employeers.append(Employee('Name ID', 'Departament', 'Id_Number', 'Job Title'))
    employeers.append(Employee("Susan Meyers", "Accounting", '47899', "Vice President"))
    employeers.append(Employee("Mark Jones", "IT", '39119', "Programmer"))
    employeers.append(Employee("Joy Rogers", "Manufacturing", '81774', "Engineer"))
    max_lenght =[0, 0, 0]
    for employee in employeers:
        if len(employee.get_name()) > max_lenght[0]: max_lenght[0] = len(employee.get_name())
        if len(str(employee.get_id())) > max_lenght[1]: max_lenght[1] = len(str(employee.get_id()))
        if len(employee.get_departament()) > max_lenght[2]: max_lenght[2] = len(employee.get_departament())
    for i in range(len(employeers)):
        print(employeers[i].get_name() + ((max_lenght[0] - len(employeers[i].get_name())+5) * " ") + employeers[i].get_id() + ((max_lenght[1] - len(employeers[i].get_id())+5)* " "), employeers[i].get_departament() + ((max_lenght[2] - len(employeers[i].get_departament())+5)* " "), employeers[i].get_job_title())
if __name__ == '__main__':
    main()
