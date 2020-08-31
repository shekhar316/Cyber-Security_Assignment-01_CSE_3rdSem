#Count UpperCase and LowerCase characters in string
def countCase(string):
    up, low = 0, 0
    for i in string:
        if(i.isupper()):
            up+=1
        elif(i.islower()):
            low+=1
    return up, low

string = input("Enter the string : ")
upCase ,lowCase = countCase(string)
print("\nNo. of Lower Case Letters : " + str(upCase))
print("No. of Lower Case Letters : " + str(lowCase))
