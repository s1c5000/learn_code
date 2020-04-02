def plus(a, b):
    if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
        return a + b
    else:
        return None

def minus(a,b):
    if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
        return a - b
    else:
        return None

def multiple(a,b):
    if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
        return a * b
    else:
        return None

def cal(a,b):
    print(plus(a,b))
    print(minus(a,b))
    print(multiple(a,b))

#cal(2,3)

cal(int(input("첫번째수 :")), int(input("두번째수 :")))
    
