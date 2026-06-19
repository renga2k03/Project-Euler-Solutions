# Q16 - Power Digit Sum

**Required Output :** Sum of digits of a power of 2 raised to a given exponent


## Idea :-
* Convert 2 to the power of given number to a string
* Change the string to a list of characters and further map the list to integer type and convert it to an integer list
* Perform summation over the integer list


## Approach :-
1) **Convert $2^n$ to a string**
2) **Change the string to a list of numeric characters and map the list entries to integer types**
3) **Find the summation of the numbers in the mapped list**

## Complexity :
**$O(t * n^2)$** (Converting the number to a string takes $O(n^2)$ time on using str() in Python)
