class Car:
    def __init__(self,year,make,speed):
        self.year = year
        self.make = make
        self.speed = speed
    def accelerate(self):
        self.speed += 5
        print("Speed after accelerate: ", self.speed)
    def brake(self):
        self.speed -= 5
        print("Speed after brake: ",self.speed)
    def get_speed(self):
        return self.speed

    def __str__(self):
        return f"Year: {self.year}, Make: {self.make}, Speed: {self.speed}"

def main():
    my_car = Car(int(input("Enter your year: ")), input("Enter your Model: "), int(input("Enter your speed: ")))
    print(my_car)
    my_car.accelerate()
    my_car.accelerate()
    my_car.accelerate()
    my_car.accelerate()
    my_car.accelerate()
    my_car.brake()
    my_car.brake()
    my_car.brake()
    my_car.brake()
    my_car.brake()
    print(my_car)
if __name__ == "__main__":
    main()