#习题19

#定义函数，并指定两个参数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheese!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
	

print("We can just give the function number directly:")
#调用函数，并直接给出确切的参数值
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script!:")
#给变量赋值
amount_of_cheese = 10
amount_of_crackers = 50

#调用函数，并用前面已赋值的变量加入到函数的参数中
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
#调用函数，参数直接用数字，同时可以用数学运算符号进行计算
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variavles amd math:")
#调用函数，并用变量加上math数据，进行参数变化
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 
