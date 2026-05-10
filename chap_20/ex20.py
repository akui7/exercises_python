#习题20

from sys import argv

script, input_file = argv

# define functon to read
def print_all(f):
	print(f.read())

# define function to seek
# I don't understand what is the '.seek', because nothing to input
# let the pointer point to the openning
def rewind(f):
	f.seek(0)

# define the function to print every line and the content	
# '.readline()' is read the current line content
def print_a_line(line_count,f):
	print(line_count, f.readline())

# open file of what you want to read	
current_file = open(input_file)

print("First let's print the whole file:\n")

# print the file content that you give the argument
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# This line can do what?
# When you read the whole file the pointer on the end
# so you need to move the pointer to the openning
# This is why need rewind 
# maybe you can try change the argument like ".seek(3) or .seek(6) watch what change
rewind(current_file)

print("let's print three lines:")

# define the current line and get the value
current_line = 1

# track the current_line 
print(f"current line is {current_line}")
print_a_line(current_line, current_file)

# The argument that current_line get the value
current_line = current_line + 1
# track the current_line 
print(f"current line is {current_line}")
print_a_line(current_line, current_file)

current_line = current_line + 1
# track the current_line 
print(f"current line is {current_line}")
print_a_line(current_line, current_file)

#close the file
current_file.close()

