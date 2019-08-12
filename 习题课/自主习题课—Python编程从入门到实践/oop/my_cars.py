"""
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2018)
print(my_beetle.get_c_name())

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_c_name())

import car
my_beetle = car.Car('volkswagen', 'beetle', 2018)
print(my_beetle.get_c_name())

my_tesla = car.ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_c_name())
"""

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2018)
print(my_beetle.get_c_name())

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_c_name())

