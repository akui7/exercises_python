#习题16 

from sys import argv

# argv 是接收命令行参数，比如` python3.6 ex16.py test.txt `
# argv 就会得到['exercise16.py', 'test.txt']
# script = 'ex16.py'     
# filename = 'test.txt'
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

# w, 如果文件不存在，python自动创建；如果文件存在，python打开他并清空内容
target = open(filename, 'w')

print("Truncating the file.	Goodbye!")

# Truncate命令是不是重复了呢？
# 重复了
# 在文档中，open()中的 ' w '模式的描述是"open for writing, truncating the file first"
# 就相当于在用 ' w '模式的时候已经truncate(截断)了一次了，所以再使用这个命令就重复了 
target.truncate()

print("Now I'm going to ask you for three lines.")

# 这里可以简化吗？
# 可以，参考ex16_2.py
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# 这里是不是可以写的简单一点？
# 可以，参考ex16_2.py
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Add finally, we close it.")
target.close()



# 1.是怎么创建这个文件的?
#	target = open(filename, 'w'),中的 " w "会创建文件

# 2.怎么简化一些看上去重复的工作呢？
#	写循环，然后将有些相似的变量变成同一个变量。

