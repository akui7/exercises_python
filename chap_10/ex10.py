#习题10		Page:31

#变量，\t是tab键位，空出8个字符
tabby_cat = "\tI'm tabbed in."

#变量，\n,换行
persian_cat = "I'm split\non a line."

# \\能打印为\,反斜杠的转义符号，将其变为打印其本身的字符
#比如   \',\" ,
backslash_cat = "I'm  \' a \\ cat." #  "I'm  \' a \" cat."

#被"""这个之间可以放入任意多行文本
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
