#习题21   作业1


# function 1
def blackbox(a, b, c):
    print(f"{a} - {b} + {c}")
    return a - b + c

# output
bbx = blackbox(1, 2, 3)
print(f"bbx = {bbx}")



# function 2
def whitebox(a, b):
    return input(f"{a} + {b}")
    
wb = whitebox(2, 3)
print(f'{wb}')

