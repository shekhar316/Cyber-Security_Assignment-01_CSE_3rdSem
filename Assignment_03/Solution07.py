def summer_69(lst,n):
    sum = 0
    flag = 0
    for i in lst:
        if(flag == 0):
            if(i == 6):
                flag = 1
            else:
                sum = sum + i
        else:
            if(i == 9):
                flag = 0
    return sum

lst = []
n = int(input("Enter the no. of element  : "))
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    lst.append(x)

print("\nsummer_69 : ",summer_69(lst,n))
