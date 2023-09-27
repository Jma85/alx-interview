#!/usr/bin/python3

from math import factorial

res = []
rows = int(input("Please enter the number of rows:"))
for i in range(rows):
    for j in range(rows-i+1):
 
# Leaving spaces on the left side.

        print(end=" ")
 
    for j in range(i+1):

# nCr formula ====> nCr = n!/((n-r)!*r!)
    
        res =  print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
# for printing a new line
    print()
