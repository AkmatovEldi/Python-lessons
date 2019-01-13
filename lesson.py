class Car:
	def __init__(self, number_of_wheels, seating_capacity, max_velocity):
		self.number_of_wheels = number_of_wheels
		self.seating_capacity = seating_capacity
		self.max_velocity = max_velocity

my_car = Car(4, 5, 250)
print(my_car.number_of_wheels)
print(my_car.seating_capacity)
print(my_car.max_velocity)

class Electric_Car(Car):
	def __init__(self, number_of_wheels, seating_capacity, max_velocity):
		Car.__init__(self, number_of_wheels, seating_capacity, max_velocity)

my_electric_car = Electric_Car(4, 5, 250)
print(my_electric_car.number_of_wheels)
print(my_electric_car.seating_capacity)
print(my_electric_car.max_velocity)