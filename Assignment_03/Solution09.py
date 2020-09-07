def count_prime(n):
    count = 0
    for i in range(2,n+1):
        flag = 0
        for j in range(2,i):
            if ((i % j) == 0):
                flag = 1
                break
        if (flag == 0):
            count += 1
    return count

n = int(input("Enter the range : "))
no_of_prime = count_prime(n)
print(no_of_prime)
