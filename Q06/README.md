# Q6 - Sum Square Difference

**Required Output :** Absolute difference between sum of squares of natural numbers upto a given number and the square of sum of all natural numbers upto the given number


## Idea :-
* Sum of first $N$ natural numbers is $\frac{N * (N + 1)}{2}$
* Sum of squares of first $N$ natural numbers is $\frac{N * (N + 1) * (2 * N + 1)}{6}$


## Approach :-
1) **Find the square of the sum of first $n$ natural numbers $sqsum$** ( $(\frac{n * (n + 1)}{2})^2$ )
2) **Find the sum of squares of first $n$ natural numbers $sumsq$** ( $\frac{n * (n + 1) * (2 * n + 1)}{6}$ )
3) **Find the absolute difference between $sumsq$ and $sqsum$**

## Complexity :
**$O(t)$**
