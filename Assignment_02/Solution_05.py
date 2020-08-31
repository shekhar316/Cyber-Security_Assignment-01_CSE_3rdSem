#multiply elemnets in list

def multiply(lst):
  answer = 1
  for i in lst:
    answer = answer * i
  return answer


lst = []
n = int(input("Enter number of elements in list : ")) 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
mult = multiply(lst)
print("\nMultiplication of all numbers in list : ", mult)
