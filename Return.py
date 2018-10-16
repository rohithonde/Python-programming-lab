def compute(a):
    print("no is", a) 
    return a*a, a*a*a
square,cube=compute(4)
print(square,cube)