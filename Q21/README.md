# Q21 - Amicable Numbers

**Required Output :** Sum of amicable numbers till a given number


## Idea :-
* Iterating through all test cases causes a TLE in case of huge number of test cases due to repetitive traversals over overlapping regions in different test cases bounds
* A single traversal from 1 till the largest number among the test cases can be done to efficiently store the solutions for each test cases in a hashmap
* Store a sorted temporary copy of the list of test cases to incrementally traverse and assign the total summation of amicable numbers till the traversal index is same as the test case value
* Likewise in Q20, the temporary copy of list must not possess any repeated numbers since the loop skips to next number and would fail to detect the multiple occurences of any number
* For each number, find the sum of its proper divisors less than itself and then repeat the same on the resultant summation as well
* Using a single function to find the sum of divisors can avoid the repetition of the factors checking part twice. Further the number of iterations can be reduced by checking only upto factors less than or equal to square root of that number
* Starting the factors' summation variable as 1, add each factor and its quotient (other factor) obtained on dividing the number by the factor
* If the number is retrieved back on performing the same operation over the resultant sum of divisors and also the number isn't equal to the sum of divisors, then include the number and its amicable pair into an array if not present already and add only the current number to the total summation variable
* In case the current number is already present in the amicable array previously detected during its smaller counterpart, then directly add it to the total summation variable
* If the traversal index equals a test case, then update the total summation value into a hashmap indexing with the current test case and move on to the next test case and next traversal index
* For each test case, retrieve the appropriate summation indexed in the hashmap


## Approach :-
1) **Store a temporary copy of the list of test cases in ascending order**
2) **While doing so, also remove the repeated values in the list by converting it into a set and then back to list**
3) **Find the maximum number $maxn$ among the test cases**
4) **Starting from 1, iterate incrementally over numbers until $maxn$ and check for amicable numbers and compute their sum**
5) **If current traversal index $n$ is already present in the amicable's list $amic$, directly add it to the total summation variable $totsum$. Otherwise go ahead and compute the sum of divisors of $n$ as $dsum1$**
6) **In the `divsum` function starting from 2 till the square root of the number, check the divisibility of numbers and if so, add the factor $i$ and its quotient on dividing the number $( n / i )$ to the summation variable $s$ which is initialized as 1 (includes 1 but excludes the number itself)**
7) **Assign $dsum1$ with the sum returned by `divsum` and further compute the sum of factors of $dsum1$ using `divsum` and assign it to another variable $dsum2$**
8) **If $dsum2$ and $n$ are equal while $dsum1$ and $n$ are distinct, then append both the numbers of the pair $n$ and $dsum1$ to an array $amic$ if they are not already present in it. Also add only $n$ to the $totsum$ variable**
9) **If given test case matches with the current index $n$, then store $totsum$ in a dictionary $tcasesum$ with the key as the current test case and move to the next test case**
10) **For each test case, print the summation indexed to it in the dictionary $tcasesum$**

## Complexity :
**$O(n\sqrt{n})$**
