# Q12 - Highly Divisible Triangular Number

**Required Output :** First triangular number to have more than a particular number of divisors


## Idea :-
* Iterating through all test cases causes a TLE in case of huge number of test cases due to potential non-linear traversal over triangular number sequence
* A single traversal over the triangular numbers upto the largest number among the test cases can be done to efficiently extract and hashmap the desired triangular number with respect to the test cases in ascending order
* Like in Q10, store a sorted temporary copy of the list cases and perform the mapping of solutions using the same
* Apart from 2, iteratively each odd numbers are checked to be prime as well as evenly dividing the traingular number until the square of the number/factor exceeds the triangular number (In other words, less than the square root of the number)
* Further reduce the number of iterations by considering only the prime factors that are already stored in the sequence and less than square root of the factor being checked
* Compute the exponent count of each prime factor of the triangular number
* The product of exponent counts of all prime factors incremented by one gives the number of factors of the triangular number


## Approach :-
1) **Store a temporary copy of the list of test cases in ascending order**
3) **Initialize $s$ as the first triangular number 1 and iterate incrementally over the subsequent triangular numbers until all test cases are covered**
4) **In the $primefactorize$ function dedicated to find the number of factors, start with prime factor $pf$ as 2 and an empty list of prime factors $pfs$**
5) **Iterate incrementally over odd numbers until the square of $pf$ is not greater than triangular number $n$ and check whether $pf$ divides $n$ and is prime or not**
6) **Check the divisibility of $pf$ with already stored prime factors in $pfs$ less than the square root of $pf$ and append $pf$ to the sequence if it is prime**
7) **Compute the number of times the prime factor $pf$ divides $n$ and store it in exponent count variable $expc$**
8) **Multiply $expc + 1$ with $c$ which would eventually store the overall count of number of factors**
9) **Handle the exception of $n = 3$ by returning 2 as the number of factors**
10) **If the returned count of factors $pfc$ exceeds the given test case, then store and map the triangular number with that test case in a dictionary $dic$**
11) **For each test case $n$, print the triangular number indexed to it in the dictionary $dic$**

## Complexity :
**$O(t * \sqrt{n})$**
