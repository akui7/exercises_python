#习题18

# def 是define（定义）的意思。定义的函数名最好能体现函数的作用.
# 将函数名定义后，需要使用" : "来结束这一行
# 冒号以下，用4个空格缩进后的内容都是函数的运行

# this one is like your script with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")
	
# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")
	
# this one takes no arguments
def print_none():
	print("I' got nothin.")


#运用上面的函数
#w为什么print_none,我把他的括号删掉后，不会报错，同时没有输出？
#因为 " print_none "的含义是应用 ' 函数对象 '本身，结果是不执行函数	==函数对象
#而 " print_none() "的含义是 ' 调用/执行函数 '，结果是执行函数体内的函数	==函数调用
#总结：括号是调用运算符
#例子：终端打开python后，退出用的不是" quit "，而是" quit() ".

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none() 

