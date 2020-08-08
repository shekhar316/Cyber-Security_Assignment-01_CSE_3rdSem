/* Name : Shekhar Saxena
  Class Roll No : 49
  University Roll No : 2014852
  Section : A 
  
  Cyber Security Assignment 01 : Question 01
  Problem Statement : Write a C/C++ program that takes n number of command line arguments and finds the least number. 
  In case of invalid entered value, prompt the user to enter another value.
  -----------------------------------------------------------------------------------------------------*/

#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[]){
    cout << "You have entered " << argc - 1 << " numbers.\n";
    int numbers[argc-1];

    //converting string to numbers
    for (int i = 1; i < argc ; i++){
        numbers[i-1] = atoi(argv[i]);
    }

    int smallest = numbers[0];
    for (int i = 1; i < argc-1 ; i++){
        if( numbers[i] == smallest ){
            cout << "Error : You have entered two same numbers. Please enter a diffrent number.";
            exit(0);
        }
        else if(numbers[i] < smallest){
            smallest = numbers[i];
        }
    }

    cout << "Smallest Number is " << smallest << endl;
    return 0;
  }
