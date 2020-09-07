def blackjack(list):
    sum = 0
    for num in list:
        sum = sum+num
    if sum <= 21:
        return sum
    else:
        flag = 0
        for num in list:
            if num == 11:
                flag = 1
                break
        if (flag == 0):
            return 'BUST'
        else:
            return sum-10


list = []
print("Input three numbers\n")
for i in range(3):
    x = int(input())
    list.append(x)
print(\nblackjack : ",blackjack(list))
