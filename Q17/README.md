# Q17 - Number to Words

**Required Output :** Write the given number in words


## Idea & Approach :-
* Store the required unique words in arrays
* Sequential terms such as the ten primary digits, tenth-words and the numbers between 10 and 20 in separate arrays for direct access like a hashmap
* Other special terms for the places such as hundredths, thousandths, millionths and billionths in another array to be accessed iteratively when required
* Use an index for the special terms and iteratively divide the given number by thousands and add the special term according to the place
* For every three digits, if the triplet exceeds hundred, include the term hundred
* For the next two digits, include the appropriate tenths-word if greater than 20 or the word forms directly for numbers from 10 to 19
* Eventually include the last individual digit at the end if not zero and not between 10 and 20
* Exclude the tenths-word and directly include the final digit word in case of zero in the tenth's place
* Also consider the case where both tenths and hundredths are zero while unit's place having a non-zero digit
* Similarly, skip the special terms if the place contains zero (such as thousandths, millionths and billionths)
* Each test case would take a maximum of 4 iterations due to the maximum possible test case being less than a trillion

## Complexity :
**$O(t)$**
