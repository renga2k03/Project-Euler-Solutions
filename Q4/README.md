# Q4 - Largest Palindrome Product

**Required Output :** Largest palindrome product of two three-digit numbers less than a given number


## Idea :-
* Iterating through all lesser numbers to check out for palindromes is tedious and guarantees a TLE
* Intuitively a palindrome can be constructed by halving the given 6 digit number and appending the reverse of the first 3 digits at the end
* Extracting the last three digits and reversing them to be appended in the front isn't much efficient since the resultant palindrome would be far away from the range of given number while the former way gives a palindrome at proximity
* Brute force approach to find the factors is very slower and TLE occurs for test cases when iterating through all 3 digit numbers
* Reduce the number of iterations by considering 3 digit numbers only upto square root of the palindrome being chosen
* If the quotient of the 3 digit factor is also a 3 digit number, the solution is achieved. Otherwise proceed to construct the next lesser 6 digit palindrome in a similar way


## Approach :-
1) **Extract the first 3 digits of given number** ( $npalin = n / 1000$)
2) **Decrementally iterate over $i$ starting from $npalin$ till 100 and append its reverse to form a resultant number $no$**
3) **Traverse through the 3 digit factors of $no$ less than square root of the $no$ and check the length of quotient $otherno$**
4) **If the quotient is also a 3 digit number, then display the palindrome product $no$ and exit the palindrome constructing outer loop**
5) **Otherwise continue building the next smaller palindrome like in Step 2 and repeat the Steps 3 and 4**

## Complexity :
**$O(n\sqrt{n})$**
