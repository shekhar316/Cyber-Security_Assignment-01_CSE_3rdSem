def fun(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if(a <= b):
            return a
        else:
            return b
    else:
        if(a >= b):
            return a
        else:
            return b

x = int(input("Enter first number  : "))
y = int(input("Enter second number : "))
res  = fun(x,y)
print("\n lesser of two events : ",res)
