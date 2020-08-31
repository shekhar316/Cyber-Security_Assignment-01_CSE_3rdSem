#  Write a function that checks whether a number is in a given range (inclusive of high and low).

def check_range(num, low, high):
    flag = 0
    for i in range(low, high + 1):
        if i == num:
            flag = 1
    if flag == 1:
        print("Number exist in given range")
    else:
        print("Number does not exist in given range")

#Main_Code

low = int(input("Enter Lower Range : "))
high = int(input("\nEnter Higher Range : "))
num = int(input("\nEnter Number to check : "))
check_range(num, low, high)
