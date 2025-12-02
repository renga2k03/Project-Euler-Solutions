# Q2 - Even Fibonacci Numbers

**Required Output :** Sum of even valued terms of Fibonacci series till a given number



## Idea :-
Each of the Fibonacci terms are obtained by adding the previous two terms and the sequence here starts with 1 and 2 as the first two terms. Add the terms to the summation variable only when even



## Approach :-
1) **Start with 1 and 2 as the first two terms and find the subsequent terms till the given number** (if $a + b < n$, $c = a + b$ )
2) **Check whether the subsequent term is even and add them to the summation variable** ( if $c mod 2 = 0$ then $s = s + c$ )
3) **Display the summation variable**

## Complexity :
**O(log n)**
