#习题14 

from sys import argv

script, user_name, year = argv
#prompt = '>'
prompt = '请输入文本:'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
And now is the {year} ,you maybe have a good computer.
Your live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""") 
