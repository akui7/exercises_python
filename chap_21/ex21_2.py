# 习题21
# input the value to calculate the result

# funciton
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtract {a} - {b}")
    return a - b    
        
def multiply(a, b):
    print(f"multiply {a} * {b}")
    return a * b
    
def divide(a, b):
    print(f"divide {a} / {b}")
    return a / b

# input what you want value of variable
# because divide is the 'str'
# so you need to use the ' float ' not ' int '
age = float(input("Your age: "))
height = float(input("Your height: "))
weight = float(input("Your weight: "))
iq = float(input("Your iq: "))

# test
#print(f"{age}, {height}, {weight}, {iq}")

print("Let's do some math with just function.")

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomse: ", what , "Can you do it by hand.")
