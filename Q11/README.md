# Q11 - Largest Product in a Grid

**Required Output :** Greatest product of four adjacent numbers in the same direction from a grid


## Idea :-
* Use flag variables for each of the four cardinal directions
* While traversing through the grid, enable the flag variables to 1 if it is possible to extract 4 continuous numbers in that direction
* Compute the product of integers extracted and compare with the previously stored maximum product to determine the largest product that can be obtained
* Brute force is applicable in this version since the test case is fixed to be 20 x 20 grid with each number being lesser than 100


## Approach :-
1) **Iterate over the grid with two loops and initialize the direction variables $up, down, left, right$ with 0**
2) **If the row index $j$ is greater than 3, assign the left variable as 1 and if less than 17, assign the right variable as 1 indicating that there are at least 3 numbers to the left or right of the cell respectively**
3) **Similarly if the column index $i$ is greater than 3, assign the up variable as 1 and if less than 17, assign the down variable as 1 indicating that there are at least 3 numbers above or below the cell respectively**
4) **If $up$ is enabled, then compute the product of 3 numbers above the current number including itself and compare with $maxprod$ to update accordingly**
5) **Further if $left$ is enabled, then compute the product of 3 numbers in the upper left diagonal including itself and compare with $maxprod$ to update accordingly**
6) **Further if $right$ is enabled, then compute the product of 3 numbers in the upper right diagonal including itself and compare with $maxprod$ to update accordingly**
7) **Repeat steps similar to 5 and 6 for the case where $down$ is enabled and compute products of lower left, lower right diagonals and downward window, and compare with $maxprod$ to update accordingly**
8) **If $left$ is enabled, then compute the product of 3 numbers to the left of current number including itself and compare with $maxprod$ to update accordingly**
9) **If $right$ is enabled, then compute the product of 3 numbers to the right of current number including itself and compare with $maxprod$ to update accordingly**

## Complexity :
**$O(1)$**
