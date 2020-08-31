#Create list of dictionary

def solve(n):
    lst =[]
    dict = {}
    for i in range(2,n+1):
        flag = 0
        for j in range(2,i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            dict[i] = "Prime"
            lst.append(dict)
        else:
            dict[i] = "Non-Prime"
            lst.append(dict)
    return lst
    
def delEle(ans1):
    count = 0
    for i in ans1:
        d = ans1[i].copy()
        for value in d.keys():
            if d[value] == "Non Prime":
            ans1.pop(i)
            c+=1
    return ans1, count

#Main_Code

n = int(input("Enter the limit : "))
ans1 = solve(n)
print("The Dictionary of all tuples upto limit is : \n",ans1)
ans2, count = delEle(ans1)
print("Dictionary after deleting elements : \n",ans2)
print("\nNo of elements deleted : ", count)
