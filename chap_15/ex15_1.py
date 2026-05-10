#习题15		作业5
#如何能直接接受第二参数？不能
#因为input()函数只能被动接收

print("输入你想打开的文件名字")
file_first = input("> ")

txt = open(file_first)

print("打印的文件内容：\n")
print(txt.read())
txt.close()

print("需要再打开一次文件吗？请再次输入文件名字")
file_again = input("> ")

txt_again = open(file_again)

print("再次打印的内容: \n")
print(txt_again.read())
txt_again.close()

