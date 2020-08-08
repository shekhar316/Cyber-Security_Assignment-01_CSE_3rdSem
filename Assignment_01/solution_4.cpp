/* Name : Shekhar Saxena
  Class Roll No : 49
  University Roll No : 2014852
  Section : A 
  
  Cyber Security Assignment 01 : Question 04
  Problem Statement : Write a C/C++ program to encrypt and decrypt the string using Caesar Cypher Algorithm. 
  While encrypting the given string, 5 is added to the ASCII value of the characters. Similarly, for decrypting 
  the string, 5 is subtracted from the ASCII value of the characters to print an original string.
  -----------------------------------------------------------------------------------------------------*/

#include <iostream> 
using namespace std; 

string encrypt(string str, int shift) 
{ 
    string result = ""; 
    for (int i = 0; i < str.length(); i++) 
    { 
        if ( isupper(str[i]) ) 
            result = result + char(int(str[i] + shift - 65) % 26 + 65); 
        else
            result = result + char(int(str[i] + shift - 97) % 26 + 97); 
    } 
    return result; 
} 

string decrypt(string str, int shift) 
{ 
    string result = ""; 
    for (int i = 0; i < str.length(); i++) 
    { 
        if ( isupper(str[i]) )  
            result = result + char(int(str[i] - shift - 65) % 26 + 65); 
        else
            result = result + char(int(str[i] - shift - 97) % 26 + 97); 
    } 
    return result; 
} 

int main() 
{ 
    string str;
    cout << "Enter a word : ";
    cin >> str;
    int shift = 5; 

    cout << "Press 1 to encrypt or 2 to decrypt : ";
    int choice;
    cin >> choice;

    cout << "\nOriginal Text : " << str; 
    cout << "\nShift: " << shift; 
    if (choice == 1){
        cout << "\nEncrypted String : " << encrypt(str, shift);    
    }
    else{
        cout << "\nDecrypted String : " << decrypt(str, shift); 
    }
     
    return 0; 
} 
