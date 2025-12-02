# Q1 - Multiples of 3 and 5

**Required Output :** Sum of all multiples of 3 or 5 below a given number



## Idea :-
Multiples of 3 and 5 are two Arithmetic Progressions and the overlapping numbers are multiples of 15 which has to be removed from the summation



## Approach :-
1) **Find the last multiple of 3, 5 and 15** which is less than the given number (considered as the last term of the APs)
2) **Find the number of terms in each APs** ( $n = \frac{(l - a)}{d} + 1$ )
3) **Find the summations of respective APs** ( $S = \frac{n}{2} (a + l)$ )
4) **Combine the summations** ( $Result = S_3 + S_5 - S_{15}$ )

## Complexity :
**O(1)**
