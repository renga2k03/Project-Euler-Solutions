# Q18 - Maximum Path Sum - I

**Required Output :** Maximum total from top to bottom of a given triangle of numbers


## Idea :-
* Tabulation approach of dynamic programming can be used to optimally compute the number of paths
* Bottom-up approach starts from the smallest subproblem and computes the other subproblems gradually having to deal the overlapping subproblems only once
* The first base case constitutes the subproblem involving the first line with a single cell with just its value being included into total
* The subsequent cases constitutes the row elements and their possible paths through their previous ancestors having the total being added up all the way through the path till then
* In case of two ancestors, the path with maximum total is chosen
* A new triangular array can be used to estimate the maximum total with respect to each lines and each cells
* The maximum total value among the final line elements gives the maximum path sum


## Approach :-
1) **Create an empty array `dist\_lines` which gradually stores the maximum path sum for each cell of each line**
3) **In case of first line, directly append the only value to $dist\_lines$**
4) **Traverse through the other lines of the triangle and calculate the maximum total for each element of the line**
5) **If the element is in either of the extremes, then directly add the previous line's total and the current value and update to the current line's array $next\_line$**
6) **Otherwise, add the current value with the maximum total among the two ancestral cells (i-1 , j-1) , (i-1 , j) and update to $next\_line$**
7) **After completing the traversal of the current line, append the array $next\_line$ to $dist\_lines$**
8) **The maximum value from the final line of $dist\_lines$ gives the required maximum path sum**

## Complexity :
**$O(t * n^2)$**
