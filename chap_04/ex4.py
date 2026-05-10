#习题4	Page:17		😍️

#定义变量（variable）,cars
cars = 100
#定义变量,
space_in_a_car = 4.0
#定义变量
drivers = 30
#定义变量
passengers = 90
#定义变量，用其他变量直接运算，相当于将右边的值传输到左边（赋值）
cars_not_driven = cars - drivers
#定义变量，将一个变量等于另一个变量
cars_driven = drivers
#定义变量，用其他变量进行运算
carpool_capacity = cars_driven * space_in_a_car
#定义变量，用其他变量进行运算
average_passengers_per_car = passengers / cars_driven

#打印句子，用变量指代数据，但没有看到直接运用变量，类似C语言那样的变量替代
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool todday.")
print("We need to put about" , average_passengers_per_car,"in each car.")


print(4 / 2)
#除法和乘法的计算会有浮点数字的计算，比如，12 / 6,显示是6.0，而不是 6。
#但是加法和减法的计算不会有浮点计算，比如 1 + 2 ,显示是3,而并不是3.0.
#" = "相当于赋值
