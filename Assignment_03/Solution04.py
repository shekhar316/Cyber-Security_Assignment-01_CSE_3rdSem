import math

def check(n):
    diff1 = abs(n-100)
    diff2 = abs(n-200)
    if(diff1 <= 10 or diff2 <= 10):
        return True
    else:
        return False

n = int(input("Enter a number : "))
print("Almost There : ",check(n))
