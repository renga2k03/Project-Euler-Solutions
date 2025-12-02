# Q3 - Largest Prime Factor

**Required Output :** Largest prime factor of given number


## Idea :-
* Brute force approach is very slower and TLE occurs for test cases when iterating through all n numbers
* Reduce the number of iterations by considering numbers only upto square root of the given number
* Further the composite numbers can be cut off by checking their divisibility with the smaller prime numbers
* Storing the prime numbers in a list over the iterations serves as a key factor in cutting off additional overhead in checking whether the factors are composite since the divisibility can be checked with just the stored prime numbers rather than every single number till the square root of the factor


## Approach :-
1) **Start with prime factor variable as 2 and an empty list of prime factors** ( $pf = 2$ and $pfs = []$)
2) **If the prime factor variable is divisible by given number, then check if the factor is prime** ( $\text{if } n \equiv 0 \pmod{pf}$ )
3) **Traverse through the prime factors list until less than square root of the $pf$ and check its divisibility with $pf$**
4) **If none of the prime factors from $pfs$ are divisible by $pf$ then update $pf$ into the list**
5) **Display the value of $pf$ after having checked till square root of given number** ( final value of $pf$ serves as the largest prime factor)

## Complexity :
**$$O(\sqrt{n})$$**
