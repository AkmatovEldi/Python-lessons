name = input("Введите имя:")
age = input("Введите возраст:")
age = int(age)
if age > 20:
	print("Вам больше 20 лет")
else:
	print("Вам {} лет".format(age))