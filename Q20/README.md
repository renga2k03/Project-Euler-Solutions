# Q20 - Factorial Digit Sum

**Required Output :** Sum of digits of factorial of a given number


## Idea :-
* Iterating through all test cases causes a TLE in case of huge number of test cases due to evaluation of factorials requiring to start over from 1 repetitively for all cases
* A single traversal from 0 till the largest number among the test cases can be done to efficiently store the solutions for each test cases in a hashmap as every integer has a unique factorial
* Store a sorted temporary copy of the list of test cases to incrementally traverse and assign the summation of digits of the factorial whenever the traversal index is same as the test case value
* Except for 0 whose factorial is 1, iteratively each numbers are multiplied onto a variable to compute the factorial with respect to each number
* However the temporary copy of list must not possess any repeated numbers since the loop skips to next number and would fail to detect the multiple occurences of any number
* For each test case, retrieve the appropriate summation indexed in the hashmap


## Approach :-
1) **Store a temporary copy of the list of test cases in ascending order**
2) **While doing so, also remove the repeated values in the list by converting it into a set and then back to list**
3) **Find the maximum number $maxn$ among the test cases**
4) **Starting from 0, iterate incrementally over numbers until $maxn$ and compute the product of numbers upto each number over the variable $f$**
5) **In case of 0, multiply $f$ (which has a default value 1) by 1. Otherwise multiply $f$ by the current index $i$ itself**
7) **If given test case matches with the current index $i$, then convert the factorial $f$ into a string and then into a list of characters**
8) **Map the list of characters as integer type, find the summation of the resultant integer array and store in a dictionary $tsoln$ with the key as the current test case**
9) **For each test case, print the summation indexed to it in the dictionary $tsoln$**

## Complexity :
**$O(n)$** (According to given test cases, the upper limit of n exceeds t and since the loops on t and maxn are seperate, the worst case constitutes maxn iterations)
