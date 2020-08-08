/* Name : Shekhar Saxena 
  Class Roll No : 49
  University Roll No : 2014852
  Section : A 
  
  Cyber Security Assignment 01 : Question 05
  Problem Statement : You are given a string (you need to take it input from user), the task is to encrypt 
this string using # and $ symbols, alternatively. While encrypting the message the encrypted format must 
repeat the symbol as many times as the letter position in alphabetical order (consider the string as case
insensitive).
  -----------------------------------------------------------------------------------------------------*/

#include <iostream> 
#include <string>
using namespace std; 

void encryptt(string str) 
{ 
    char pos1 = '#';
    char pos2 = '$'; 
    int number_of_char, ascii; 
  
    for (int i = 0; i <= str.length(); i++)  
    { 
        char ascii = str[i]; 
        number_of_char = ascii >= 97 ? ascii - 96 : ascii - 64; 
        for (int j = 0; j < number_of_char; j++) 
        { 
            if (i % 2 == 0) 
                cout << pos1; 
            else
                cout << pos2; 
        } 
    } 
} 

int main() 
{ 
    string text;
    cout << "Enter a word to encrypt : ";
    cin >> text;
    cout << "Encrypted Text : "; 
    encryptt(text); 
    return 0; 
} 
