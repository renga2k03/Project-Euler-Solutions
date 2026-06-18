# Q13 - Large Sum

**Required Output :** First 10 digits of final sum over a particular number of 50 digit numbers


## Idea :-
* Last 40 digits and first 10 digits can be extracted and added separately
* The carry over from the sum of 40 digits needs to be added to the summation of first 10 digits
* Extract the first 10 digits from the computed summation which could exceed 10 digits due to the carry overs in the addition


## Approach :-
1) **Compute and store the sum of first 10 digits and last 40 digits** ( $n$ mod $10^{40}$ and $n$ / $10^{40}$ )
2) **Add the carry over from the sum of 40 digits ( $last40$ / $10^{40}$ ) to $first10$**
3) **Find the first 10 digits from the above resultant sum** ( divide by $10^{$length of first10$ - 10}$ )

## Complexity :
**$O(n * 50)$**
