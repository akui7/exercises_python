#习题6	Page:22

#变量赋值，然后用字符串在字符中体现		(1）
types_of_people = 10
x = f"There are {types_of_people} types of people."

#将变量赋值，然后在用字符串，将变量赋值	（2，3）
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#打印变量
print(x)
print(y)

#打印字符串，如果把前面的" f "删掉会发生什么呢?	（4,5）
print(f"I said: {x}")
print(f"I also said:'{y}'")

#变量赋值
#hilarious = False
hilarious = True
joke_evaluation = "Isn't that joke so funny?!{}"

#打印变量，并使用了.format,来作为变量的使用	(6)
print(joke_evaluation.format(hilarious))

#将字符串赋值给变量w和e
w = "This is the left side of..."
e = "a string with a right side."

#打印这段字符，将w 和 e的内容放在一起。(只是将两个变量的值，拼接在一起)
print(w + e)
