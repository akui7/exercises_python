#习题16 作业3

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input(">>> ?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.    Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

#输入 原版本 
#line1 = input("line 1:")
#line2 = input("line 2:")
#line3 = input("line 3:")

#输入 版本1
#循环的第一种写法
#lines = []
#for i in range(3):
#	lines.append(input(f"line{i+1}: "))

#输入 版本2
#循环的第二种写法
lines = [input(f"line{i+1}: ") for i in range(3)]

print("I'm going to write these to the file.")

#输出 版本1 测试完成
#使用的是字符串
#target.write(f"{line1}\n{line2}\n{line3}\n")

#输出 版本2 测试完成
#查询 " join " 的用法
#target.write("\n".join([line1, line2, line3]) + "\n")

#输出 版本3 测试完成
#用 " + "来串联多行输出
#target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#输出 版本4 测试完成
#配合输入的lines变量,与循环配合使用
#join希望得到的是字符串，不能再让他得到一个列表，所以不能用.join([lines])
target.write("\n".join(lines) + "\n")


print("And finally, we close it.")
target.close() 
