#find unique elemnets in list

def findUnique(oldList):
  newList = []
  for i in oldList:
    if i not in newList:
      newList.append(i)
  return newList


oldList = []
n = int(input("Enter number of elements in list : ")) 
for i in range(0, n): 
    ele = int(input()) 
    oldList.append(ele)
print("\nOriginal List", oldList)
newList = findUnique(oldList)
print("Unique elements in List : ",newList)
