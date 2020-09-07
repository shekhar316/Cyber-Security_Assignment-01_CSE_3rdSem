def spy_game(lst,n):
    search = 0
    flag = 0
    for i in lst:
            if (i == search):
                flag = flag + 1
            if (flag == 1):
                search = 0
            if (flag == 2):
                search = 7
    if (flag >= 3):
        return True
    else:
        return Flase

lst = []
n = int(input("Enter the no. of element  : "))
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    lst.append(x)

print("\nspy_game : ",spy_game(lst,n))
