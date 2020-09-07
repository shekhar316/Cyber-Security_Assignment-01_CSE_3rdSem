def check(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            print("\nThis is not a Pangram String")
    return print("\nThis is a Pangram String ")

str = input("Enter the string : ")
check(str)
