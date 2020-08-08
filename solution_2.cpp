/* Name : Shekhar Saxena
  Class Roll No : 49
  University Roll No : 2014852
  Section : A 
  
  Cyber Security Assignment 01 : Question 02
  Problem Statement : Write a C/C++ program to check whether a string is palindrome or not. 
  -----------------------------------------------------------------------------------------------------*/

#include <iostream>
#include <string>
using namespace std;

int main(){
    string str;
    cout << "Enter a string to check Palindrome : "; 
    cin >> str; 
    int flag = 1, i, j;
    for( i = 0,  j = str.length()-1 ; i < (str.length()/2); i++, j--){
        if(str[i] != str[j]){
            flag = 0; 
            break;
        } 
    }
    if( flag == 0){
        cout << "String is not Palindrome.\n";
    }
    else{
        cout << "String is Palindrome.\n";
    }
    return 0;
  }
