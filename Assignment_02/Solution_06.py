#string is palindrome or not

def isPalindrome(string):
	i = 0
	j = len(string) - 1
	flag = 0
	while j >= i:
		if not string[i] == string[j]:
		    flag = 1
			
		i += 1
		j -= 1
	if (flag == 1):
	    print("String is not palindrome.")
	else:
	    print("String is Palindrome.")
	    
st = input("Enter the string : ")
isPalindrome(st) 
