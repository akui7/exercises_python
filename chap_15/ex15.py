#习题15

#将sys 模块启动
from sys import argv

#将argv中的两个参数分别赋给script和filename
#argv是列表，不是函数
script, filename = argv

#调用open函数打开文件，返回的文件对象赋给txt
#是先打开，得到文件对象，再赋值
txt = open(filename)

#输出将要打开的文件名字
print(f"Here's your file {filename}:")
#调用txt文件对象的.read()方法，读取文件全部内容并打印
#.read()不是独立的函数，而是文件对象的方法
print(txt.read())
#关闭打开的文件，直接调用已定义的变量
txt.close()

#输出
print("Type the filename again:")
#接收用户输入并赋值给file_name
file_again = input("> ")

#将txt_again定义变量，并且打开由input接收到的文件名
txt_again = open(file_again)

#将接收到的文件打开并输出到终端。
print(txt_again.read())
#关闭打开的文件，直接调用已定义的变量
txt_again.close()
