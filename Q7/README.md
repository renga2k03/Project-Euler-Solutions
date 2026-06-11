# Q7 - 10001st Prime

**Required Output :** Nth prime number


## Idea :-
* Iterating through all test cases causes a TLE in case of huge number of test cases due to redundant storage of prime number sequences
* One single sequence of primes upto the largest number among the test cases can be maintained to efficiently store primes as well as seperate the test case iterations from the prime checking segment
* Apart from 2, iteratively each odd numbers are checked to be prime or not until the maximum required sequence length among the test cases is reached
* Further reduce the number of iterations by considering only the prime factors that are already stored in the sequence and less than square root of the number being checked
* For each test case, retrieve the appropriate prime number indexed in the sequence


## Approach :-
1) **Find the maximum number among the test cases $maxn$**
2) **Initially with $no$ as 2, iterate incrementally over odd numbers until the length of prime numbers sequence $pfs$ is less than $maxn$ and check whether $no$ is prime or not**
3) **Check the divisibility of $no$ with already stored prime factors in $pfs$ less than the square root of $no$ and append to the sequence if it is prime**
4) **For each test case $c$, print the $c - 1$-th number from prime number sequence $pfs$**

## Complexity :
**$O(t + n\sqrt{n})$**
