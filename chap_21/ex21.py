# 习题21

# function add, subtract, multiply, divide
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
    
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
        
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIDVIDE {a} / {b}")
    return a / b
    

print("Let's do some math with just function!")

#  value of variavle
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(50, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# way 1
#what = add(age, subtract(height,multiply(weight,divide(iq, 2))))

#print("That becomse: ", what, "Can you do it by hand?")

# In the way 2 
# why? the output is different
# ' print(f"{d} {m} {s} {a}") ' and ' print(f"{a}") '
# should output twice the prints
# but just without the " 12.5 2250.0 -2176.0 -2141.0 "

# way 2
d = divide(iq, 2)
m = multiply(weight,(d + 2))
s = subtract(height,(m * 2))
a = add(age, (s / 2))

#print(f"{d} {m} {s} {a}")
print("That becomse: ",a,"Can you do it by hand?")

# way 3
x = (age + (height - (weight * (iq / 2))))

print("That becomse: ", x ,"Can you do it by hand?")










