#习题16 作业2

from sys import argv

script, filename = argv

py = open(filename)

# 加了' f ' python才能去分普通字符串和需要做变量替换的字符串
# 没有' f ' {filename}只是普通字符，不是变量插值 
print(f" You open the file {[filename]}")
print('--------------------------------')
print(py.read())
py.close()

