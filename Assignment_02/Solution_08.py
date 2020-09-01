#Create list of dictionary

n = int(input("Enter the limit : "))
dict = {}

for i in range(2,n+1):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            dict[i] = "Non Prime"
            break
    if flag == 0:
        dict[i] ="Prime"
        
print("The dictionary is : ",dict)

count = 0
dict2 = dict.copy()

for value in dict2.keys():
    if dict2[value] == "Non Prime":
        dict.pop(value)
        count+=1
print("The dictionary with Prime Numbers  is : ",dict)
print("The total Non Prime values are : ",count)
