#习题8	Page:27

#定义一个名为"formatter"的函数（function）
formatter = "{} {} {} {}"

#打印内容，调用formattera函数，并将1,2,3,4依次传入函数，并返回。
print(formatter.format(1, 2, 3, 4))

#打印内容，调用formatter函数，并将其内容依次传入函数，并返回
#因为不是关键字，所以需要" 和 '来表明是字符串
print(formatter.format("one", "two", "three", "four"))

#打印内容，调用函数，并将内容传入函数，并返回。
#但是由于Ture和Flase是python的关键字，所以不用"和'来表明字符串
print(formatter.format(True, False, False, True))


print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poam",
	"Or a song about fear"
	
))
