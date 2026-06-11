# Q9 - Special Pythagorean Triplet

**Required Output :** Largest possible product of a Pythagorean triplet whose summation is the given number


## Idea :-
* Iterating through three variables for each of the triplets to find out the validity and maximum product is tedious and guarantees a TLE
* Even iterating through two variables and calculating the third one using the two variables and given sum also causes TLE with respect to given test cases
* Out of the four variables, the summation is given and by considering one among the triplets to be iterated over a range, there will be two equations on the remaining two variables and solving them is possible by substitution method and quadratic formula
* Moreover the product can be calculated using just one of the triplets and the given summation. But finding out the remaining triplets is necessary to evaluate the validity of the selected triplet being Pythagorean or not
* Also the Pythagorean triplets represent sides of a traingle so that neither of them can be zero and any one of the triplets can never exceed the sum of the other two triplets
* The range of iterations to be considered for one of the triplets can be reduced to start from one-third of the given summation till the half of given summation using above conditions
* The product of the valid triplets are compared with any such previous valid triplet products to find the largest one and in case of no valid triplets to exist, appropriate output is shown


## Approach :-
1) **Initialize the maximum product with -1 to handle the case where no valid triplets exists** ( $maxprod = -1$ )
2) **Iterate over the third triplet $c$ starting from one-third of given number $n/3$ till half of the given number $n/2$**
3) **Compute the product $prod$ using given number and the triplet** ( $prod = n^2 * (2 * n * c) * c / 2$ )
4) **Before solving the quadratic equation of the other two triplets, check the discriminant $d$ to be non negative to avoid imaginary solutions** ( $d = c^2 - n^2 + 2 * n * c$ )
5) **Calculate the solutions for other two triplets $a$ and $b$ using quadratic formula** ( $a = ((n - c) - \sqrt{d}) / 2$ and $b = ((n - c) + \sqrt{d}) / 2$)
6) **Check the validity of the triplets $a$, $b$, and $c$ and update the product if it exceeds the previous value of $maxprod$**

## Complexity :
**$O(t * n)$**
