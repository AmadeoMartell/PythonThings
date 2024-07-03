class Person:
    def __init__(self, name='', adress="", age=0, phone=''):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = adress

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_phone(self):
        return self

    def get_adress(self):
        return self.address

    def set_adress(self, adress):
        self.address = adress

    def __str__(self):
        return f'ПЕРСОНАЛЬНЫЕ ДАННЫЕ {(self.name).upper()}:\nВозраст:{self.age}:\nНомер телефона:{self.phone}:\nАдрес дома:{self.address}\n'


def main():
    person_list = []
    for i in range(0, 3):
        person_list.append(Person())
        print(f"Введите данные человека №{i + 1}: ")
        person_list[i].set_age(int(input("Возраст: ")))
        person_list[i].set_name(input("Имя человека: "))
        person_list[i].set_phone(input("Номер телефона: "))
        person_list[i].set_adress(input("Его адрес: "))
    for person in person_list:
        print(person)


if __name__ == '__main__':
    main()
