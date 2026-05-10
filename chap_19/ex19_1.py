#习题19	作业

# 因为chicken和duck数量都为整数，所以我在函数定义这里直接用int(整型)
# 这样后面调用函数的参数无论是什么数据类型，最终输出都是整型
# 
def chicken_and_duck(chicken_number, duck_number):
	# 返回字符串，并且打印。 函数版本 2
	result = (	f"Chicken have {int(chicken_number) * 2} legs\n"
				f"Duck have {int(duck_number) * 4} legs\n"
				f"So you have {int(chicken_number) * 2 + int(duck_number) * 4} legs\n"
				f"-----------------------------------------------\n\n")
	print(result, end='')
	return result

'''
	# 正常打印 函数版本 1
	print(f"Chicken have {int(chicken_number) * 2} legs")
	print(f"Duck have {int(duck_number) * 4} legs")
	print(f"So you have {int(chicken_number) * 2 + int(duck_number) * 4} legs")
	print("-----------------------------------------------\n")
'''
	
# 0
print(">>> 0: ")
chicken_and_duck(1, 2)


# 1
print(">>> 1: ")
chicken_and_duck(2^2, 3*4)


# 2
# 这里不能直接用input接收数据，因为input默认接收的数据是str(字符串类型)
# 这就导致定义的函数用的 " *2 " 就会被重复，相当于是将 " 字符串重复n次 "
# 比如 我输入chicken的是 ' 2 ',输出就是 ' 22 ',相当于将字符串重复了2次
# 所以要在接收输入的前面加入int(整数)，将" 字符串型 "变换为" 整数型 "
print(">>> 2: ")
chicken = int(input("chicken = "))
duck = int(input("duck = "))

chicken_and_duck(chicken, duck)


# 3
print(">>> 3: ")

# 这里可以检验输入吗？让chicken和duck的输入变得更现实一点
# 比如chikcen_leg为2的倍数，且不能等于1，等于0时，自动将chicken_number变为0
chicken_legs = int(input("chicken_leg = "))
duck_legs = int(input("duck_leg = "))

chicken_and_duck(chicken_legs/2, duck_legs/4)

'''
# 4

# 首先是，提示将要将内容写入文件
# 接着是变量赋值，先询问文件名字，然后将用 ' w '模式写入输入的文件名字
# 然后将变量用 '.write'写入，用自己定义的函数
# 思路没有问题。但是我在 '函数版本 1'遇到了问题。
# 因为，'.write'需要一个返回值，并且是str。
# 而我的函数内容时打印，没有返回值。
# 所以无法正常使用' .write '
# 接着我就用ai，将其改为了'函数版本 2'，能输出字符串，并且能打印到终端的代码。
print(">>> 4: ")
input("Input the number and write to the file...")
file_w = open(input(">>> filename ="), 'w')

ch_h = int(input("chicken_head = "))
du_h = int(input("duck_head = "))

file_w.write(chicken_and_duck(ch_h, du_h))

file_w.close() 
'''

# 5
print(">>> 5: ")


