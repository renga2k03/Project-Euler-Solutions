# Q8 - Largest Product in a Series

**Required Output :** Greatest product of k consecutive digits of a large number


## Idea :-
* Treat the large number as a string array and extract the numbers by a window of length of the given number
* Compute the product of integers in the window and compare with the previous window's product to determine the largest product that can be obtained
* Brute force is applicable in this version since the test cases are not very large, particularly the number of consecutive digits to be considered is given to be less than or equal to 7


## Approach :-
1) **Convert the given large number $num$ to a list of strings with each digit as a character**
2) **Iterate over the converted number $l$ as long as the starting index $i$ of window is $k$ less than the length of number to avoid going out-of-bounds**
3) **Extract the window $win$ upto k characters and iterate over the window to compute the product $prod$**
4) **With maximum product $maxprod$ being initialized as 0, compare with the computed product and update when it exceeds $maxprod$**
5) **Repeat the steps 3 and 4 till the window reaches the end**

## Complexity :
**$O(t * n * k)$**
