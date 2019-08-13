from car import Car

my_new_car = Car('audi', 'a12', 2022)
print(my_new_car.get_c_name())
my_new_car.odometer_reading = 20
my_new_car.read_odometer()

