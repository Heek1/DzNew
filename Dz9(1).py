import random

def fun():
    x=[]
    for i in range(10):
        x.append(random.randint(-100,100))
    print(x)
    return x



def work():
    max=fun()[0]
    min=fun()[0]
    for i in fun():
        if i > max:
            max = i
        if i < min:
            min = i
    print(f"your max number is {max}")
    print(f"your min number is {min}")

print(work())
