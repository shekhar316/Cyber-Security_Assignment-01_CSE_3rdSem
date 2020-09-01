#print fibbonacci series upto n (entered through command line)
import sys
n = int(sys.argv[1])
num1, num2 = 0, 1
count = 0

print("First ", n , " terms of Fibonacci series :")

while count < n:
    print(num1)
    num = num1 + num2
    num1 = num2
    num2 = num
    count += 1
