# Q5 - Smallest Multiple

**Required Output :** Smallest number that is evenly divisible by all positive integers less than a given number


## Idea :-
* The product of all positive numbers less than a given number would not be the smallest common multiple due to numbers being composite
* To find out the least common multiple of all these numbers, the composite numbers have to be broken down to their prime factorization forms
* Like in previous questions, the prime or composite check is done upto factors less than square root of the number to lessen iterations and the composite numbers are chosen to be prime factorized
* This converts the overall product to be of only prime factors but with most of them having repeated occurences in multiple prime factor trees
* The highest power of the prime factors among all the prime factor trees is considered to ensure the final product being minimum


## Approach :-
1) **Create a dictionary/hashmap to store the count of each prime factors** ( $pfs = /{/}$ )
2) **Iterate over all numbers $i$ till given number $n$ and assign flag variable $f = 0 or 1$ accordingly to determine whether they are composite or not**
3) **If prime, then directly assign the number to $pfs$ and initialize with 1**
4) **If composite, then break down the number with respect to each prime factor $j$ stored as keys in $pfs$ and determine the factor's count $ct$ till it divides the number $i$**
5) **If the final count of that prime factor exceeds the count already assigned in $pfs$ then update it with the new count $ct$**
6) **Perform steps 5 and 6 until the number $i$ is completely factorized down**
7) **Multiply all the prime factors from the dictionary $pfs$ raised to the power of their counts to get the smallest multiple that divides all positive integers upto the given number**

## Complexity :
**$O(n\sqrt{n})$**
