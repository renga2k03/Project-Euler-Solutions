# Q23 - Non-Abundant Sums

**Required Output :** If a given number can be expressed as a sum of two abundant numbers


## Idea :-
* Iterating through all test cases causes a TLE in case of huge number of test cases due to repetitive traversals over overlapping regions in different test cases bounds
* A single traversal from 1 till the largest number among the test cases can be done to efficiently store the solutions for each test cases in a hashmap
* Store a sorted temporary copy of the list of test cases to incrementally traverse and check the number to be a sum of two abundant numbers when the traversal index is same as the test case value
* Likewise in Q21, the temporary copy of list must not possess any repeated numbers since the loop skips to next number and would fail to detect the multiple occurences of any number
* For each number, find the sum of its proper divisors less than itself
* The number of iterations can be reduced by checking only upto factors less than or equal to square root of that number
* Starting the factors' summation variable as 1, add each factor and its quotient (other factor) obtained on dividing the number by the factor
* If the number is less than the sum of divisors, then include the number into an array to store abundant numbers
* Since the smallest abundant number is 12, test cases that are less than 12 can be guaranteed impossible to be expressed as sum of two abundant numbers and hence can directly assign the solution as not possible
* If the traversal index equals a test case, then subtract each known abundant number from the test case at a time and check if the result is also present in the abundant numbers' array
* If the result is also an abundant number, then assign the solution as possible and move on to the next test case and next traversal index
* If none of the abundant numbers when subtracted could bring up another abundant number as result, then assign the solution as not possible and proceed to the next test case
* For each test case, retrieve the appropriate solution indexed in the hashmap


## Approach :-
1) **Store a temporary copy of the list of test cases in ascending order**
2) **While doing so, also remove the repeated values in the list by converting it into a set and then back to list**
3) **Find the maximum number $maxn$ among the test cases**
4) **Starting from 1, iterate incrementally over numbers until $maxn$ and check for abundant numbers and store them in an array $abundant$**
5) **If current test case value is less than 12, directly assign "NO" as the solution in a dictionary $tcasesoln$ with the key as the current test case and move to the next test case**
6) **For other values of traversal index $n$, compute the sum of factors using `divusom` and check if it exceeds $n$**
7) **In the `divsum` function starting from 2 till the square root of the number, check the divisibility of numbers and if so, add the factor $i$ and its quotient on dividing the number $( n / i )$ to the summation variable $s$ which is initialized as 1 (includes 1 but excludes the number itself)**
8) **If the sum returned by `divsum` exceeds $n$, include the number $n$ into an array $abundant$**
9) **If given test case matches with the current index $n$, then assign a flag variable as 0 initially and iterate over all known abundant numbers to check if when subtracted from $n$ gives an abundant number present in $abundant$**
10) **If present, assign $flag$ as 1 and assign "YES" to the current test case in the dictionary $tcasesoln$ and move to the next test case**
11) **Otherwise if none of the numbers could end up with an abundant number as the result when subtracted from $n$ and the $flag$ stays as 0, then assign "NO" to the current test case in the dictionary $tcasesoln$ and move to the next test case**
12) **For each test case, print the summation indexed to it in the dictionary $tcasesum$**

## Complexity :
**$O(n\sqrt{n})$**
