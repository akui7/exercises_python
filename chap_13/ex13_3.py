#习题13 作业
#将input和argv一起使用

#需要将sys 这个模块移动到变量上，才能使用。同时这个变量是固有变量(argv)
from sys import argv
script, akui, acai = argv

#用input，去强调得到的输入
token = input(" This is the input function to get the argvment,\n you need to input 1 or 3 \n > ")

#input的输出
print(f" Input is {token} ")
#argv的输出
print(" The other get argvments is called:", script)
print(" The fake name:", akui)
print(" the good name:", acai)

