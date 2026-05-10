#习题7	Page:25

#打印内容
print("Mary had a little lamb.")

#打印内容
#只是一个内容为snow的字符串
print("Its fleece was white as {}.".format('snow'))

#打印字符
print("And everywhere that Mary went.")

#他将 " . "连续重复了10次
print("." * 10)		# what'd that do?

print(" ! " * 2)

print(":)" * 6)


end1 =  "C"
end2 =  "h"
end3 =  "e"
end4 =  "e"
end5 =  "s"
end6 =  "e"
end7 =  "B"
end8 =  "u"
end9 =  "r"
end10 = "g"
end11 = "e"
end12 = "r"


# watch that comma（逗号） at the end.	try removing it to see what happens
#删掉后，不是连在一起了，而是像之前的输出一样分为两行

#end=''就好像将下面打印的end值，放在同一行了。
print(end1 + end2 + end3 + end4 + end5 + end6 ,end='')
#print(end1 + end2 + end3 + end4 + end5 + end6 )
print(end7 + end9 + end9 +end10 + end11 + end12)
