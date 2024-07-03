class RetailItem:
    def __init__(self, Description='', Units="", Price=''):
        self.Description = Description
        self.Units = Units
        self.Price = Price
    def setDescription(self, Description):
        self.Description = Description
    def setUnits(self, Units):
        self.Units = Units
    def setPrice(self, Price):
        self.Price = Price
    def getDescription(self):
        return self.Description
    def getUnits(self):
        return self.Units
    def getPrice(self):
        return self.Price

# Susan Meyers 47899 Accounting Vice President
# Mark Jones 39119 IT Programmer
# Joy Rogers 81774 Manufacturing Engineer
def main():
    Items = []
    Items.append(RetailItem("Description", "Units in Inventory", "Price"))
    Items.append(RetailItem("Jacket", "12", "59.95"))
    Items.append(RetailItem("Designer Jeans", "40", "34.95"))
    Items.append(RetailItem("Shirt", "20", "24.95"))

    max_lenght =[0, 0]
    for employee in Items:
        if len(employee.getDescription()) > max_lenght[0]: max_lenght[0] = len(employee.getDescription())
        if len(str(employee.getUnits())) > max_lenght[1]: max_lenght[1] = len(str(employee.getUnits()))

    for i in range(len(Items)):
        print(f'{"Item #" + str(i) + " "*8 if i != 0 else " "*15}'+ Items[i].getDescription() + ((max_lenght[0] - len(Items[i].getDescription())+8) * " ") + Items[i].getUnits() + ((max_lenght[1] - len(Items[i].getUnits())+8)* " ") + Items[i].getPrice())
if __name__ == '__main__':
    main()
