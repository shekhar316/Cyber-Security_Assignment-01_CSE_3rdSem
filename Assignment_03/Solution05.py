def has_33(list):
    for num in range(0,len(list)-1):
        if list[num] == 3 and list[num + 1] == 3:
            return True
    return False

n = int(input("Enter numbers : "))
list = []
for i in range(n):
    x = int(input())
    list.append(x)

print("has_33 : ", has_33(list))
