class Pet:
    def __init__(self, name='', animal_type='', age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    my_pet = Pet()

    name = input("Enter your pet's name: ")
    animal_type = input("Enter the type of your pet (e.g., Dog, Cat, Bird): ")
    age = input("Enter your pet's age: ")


    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)


    print("\nPet's Details:")
    print(f"Name: {my_pet.get_name()}")
    print(f"Type: {my_pet.get_type()}")
    print(f"Age: {my_pet.get_age()}")


if __name__ == "__main__":
    main()
