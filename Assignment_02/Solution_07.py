
def solve(n):
    lst = []
    for i in range(2,n+1):
        flag = 0
        for j in range(2,i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            tup = (i,'Prime')
            lst.append(tup)
        else:
            tup = (i,'Non Prime')
            lst.append(tup)
    return lst

#Main_Code

n = int(input("Enter the limit : "))
ansList = solve(n)
print("The list of tuples is : \n",ansList)
