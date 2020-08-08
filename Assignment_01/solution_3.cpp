/* Name : Shekhar Saxena
  Class Roll No : 49
  University Roll No : 2014852
  Section : A 
  
  Cyber Security Assignment 01 : Question 03
  Problem Statement : Write a C/C++ program that lists down all the prime numbers in a range between a and b, 
  where a and b are two whole numbers.
  -----------------------------------------------------------------------------------------------------*/

#include <iostream>
using namespace std;

int is_prime(int x){
    int flag = 1;
    for(int i = 2; i <= x/2; i++)
    {
        if (x % i == 0)
        {
            flag = 0;
            break;
        }
    }
    return flag;
}

int main(){
    int a, b;
    cout << "Enter limits : ";
    cin >> a >> b;
    cout << "Prime Number between " << a << " and " << b << " are : ";

    for(int i = a+1; i < b; i++){
        int flag = is_prime(i);
        if(flag = 1){
            cout << i << " ";
        }
    }

    return 0;
  }
 
