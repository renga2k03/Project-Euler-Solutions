# Q15 - Lattice Paths

**Required Output :** Number of paths possible from top left corner to bottom right corner of a grid


## Idea :-
* Tabulation approach of dynamic programming can be used to optimally compute the number of paths
* Bottom-up approach starts from the smallest subproblem and computes the other subproblems gradually having to deal the overlapping subproblems only once
* Iterating through all test cases causes a TLE in case of huge number of test cases due to redundant storage of multiple grid subproblems
* Utilize a single grid with the biggest dimensions among the test cases
* The first base case constitutes the subproblem involving a single cell with requires 2 paths
* The next base cases constitutes the first row and first column requiring paths gradually incrementing over 2 towards the end
* The number of paths in other cases involve summing the number of paths till the cell above them and left of them


## Approach :-
1) **Find the maximum dimensions $maxn$ and $maxm$ among the test cases**
2) **Create a grid of dimensions $maxn$ and $maxm$ with cells storing 0 initially**
3) **Start the first cell $grid[0][0]$ with 2 and gradually increment it over the first row and first column respectively**
4) **Traverse through the other cells of the grid starting from (1, 1) till bottom right corner $(maxn, maxm)$**
5) **Assign each cell the sum of values in the cells to the left and above**
6) **For each test case, extract the value stored in the grid cell indexed to the test case dimensions**

## Complexity :
**$O(t + n * m)$**
