# Q25 - N-Digit Fibonacci Number

**Required Output :** First N digit Fibonacci number


## Idea :-
* Iterating through all test cases causes a TLE in case of huge number of test cases due to repetitive traversals over overlapping regions in different test cases bounds
* A single traversal from 1 till the largest number among the test cases can be done to efficiently store the solutions for each test cases in a hashmap
* Store a sorted temporary copy of the list of test cases to incrementally traverse and assign the Fibonacci number's index (or position in the Fibonacci series) when the number of digits is same as the test case value
* Likewise in Q23, the temporary copy of list must not possess any repeated numbers since the loop skips to next number and would fail to detect the multiple occurences of any number
* Initially with a and b as 1 being the first two terms and also having n as 2 to indicate b as the 2nd number of the series, compute the subsequent numbers of the series as the sum of the two previous numbers
* However computing the number of digits of very huge numbers that exceed 4300 digits can cause memory exceptions when converting them to a string list and calculating the length. Also TLEs occur when looping over 1000s of digits for 1000s of test cases to find the number of digits by integer division by 10
* Hence a variable is maintained to store the number of digits. Initially being 1, the variable increments when the Fibonacci number exceeds 10 to the power of previous value of the variable
* If the number of digits variable equals a test case, then update the Fibonacci number's position into a hashmap indexing with the current test case and move on to the next test case and next traversal index
* For each test case, retrieve the appropriate position of the Fibonacci number indexed in the hashmap


## Approach :-
1) **Store a temporary copy of the list of test cases in ascending order**
2) **While doing so, also remove the repeated values in the list by converting it into a set and then back to list**
3) **Find the maximum number $maxn$ among the test cases**
4) **Starting the number of digits variable $ndigits$ from 1, iterate incrementally over numbers until $maxn$ and till all test cases from $tsorted$ are checked $( i < len(tsorted) )$**
5) **With $a$ and $b$ being initially 1 and $n$ as 2, compute $c$ as $( a + b)$ and assign $b$ to $a$ and $c$ to $b$ for the next iteration and also increment $n$ by 1**
6) **If $b$ is greater than or equal to $10^{ndigits}$, then increment $ndigits$ by 1**
7) **If given test case matches with $ndigits$, then store the position of Fibonacci number $n$ in a dictionary $tsoln$ with the key as the current test case and move to the next test case**
10) **For each test case, print the position of Fibonacci number indexed to it in the dictionary $tsoln$**

## Complexity :
**$O(n^2)$** (Despite the main loop taking just n iterations, the big int additions over 5000 digit long numbers can be equivalent to the complexity of n iterations)
