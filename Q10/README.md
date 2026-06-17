# Q10 - Summation of Primes

**Required Output :** Sum of all primes not greater than given number


## Idea :-
* Iterating through all test cases causes a TLE in case of huge number of test cases due to redundant storage of prime number sequences
* Similar to Q8, a single sequence of primes upto the largest number among the test cases can be maintained to efficiently store primes as well as seperate the test case iterations from the prime checking segment
* Apart from 2, iteratively each odd numbers are checked to be prime or not until the maximum required sequence length among the test cases is reached
* Further reduce the number of iterations by considering only the prime factors that are already stored in the sequence and less than square root of the number being checked
* Store a sorted temporary copy of the list cases to incrementally traverse the prime number sequencev and slice out the summation while avoiding any backtracking of the slicing index
* For each test case, retrieve the appropriate summation indexed in the hashmap


## Approach :-
1) **Store a temporary copy of the list of test cases in ascending order**
2) **Find the maximum number $maxn$ among the test cases**
3) **Initially with $no$ as 2, iterate incrementally over odd numbers until the length of prime numbers sequence $pfs$ is less than $maxn$ and check whether $no$ is prime or not**
4) **Check the divisibility of $no$ with already stored prime factors in $pfs$ less than the square root of $no$ and append $no$ to the sequence if it is prime**
5) **Iterate over $pfs$ as long as all test cases are covered ($j < t$)**
6) **If given test case is a prime number in $pfs$, then slice the summation from $pfs$ including the number and store in a dictionary $dic$**
7) **Otherwise slice the summation from $pfs$ upto primes less than the given test case and store in a dictionary $dic$**
8) **For each test case $n$, print the summation indexed to it in the dictionary $dic$**

## Complexity :
**$O(t + n\sqrt{n})$**
