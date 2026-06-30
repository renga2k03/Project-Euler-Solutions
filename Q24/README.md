# Q24 - Lexicographic Permutations

**Required Output :** Nth lexicographic permutation of the word "abcdefghijklm"


## Idea :-
* Computing and iterating through all permutations of the given word can be tedious and cause TLE due to huge number of iterations and even the memory space required to store them which could go up to 13!
* As the word is already given to be "abcdefghijklm", store the characters of the word in an array and also all factorials upto 13 in another array
* Each factorial from 1 to 13 indicates the number of shuffles or permutations possible in characters from 1 to 13 positions respectively
* To identify the number of characters to be shuffled for the given position N, find the largest factorial that is less than the given number
* Seperate the entire word into two arrays, one for the unshuffled characters with respect to the test case and other for the characters to be shuffled which comprises the entities from the position where the given number exceeds the factorial
* From left to right in the shuffled array, the number of possible letters in each position would decreases from being possible to place any letters in the lefmost position to being able to place only the remaining one character in the rightmost position
* To find out the shuffle step count of each position, divide the given position N with the factorial of each position (permutation count) to find the step count of shuffle and append the letter to the unshuffle list while popping it out from the shuffle list.
* Also proceed to the next position with the remainder obtained when N is divided by the factorial of that position
* But if the factorial exactly divides N, then consider the shuffle step count to be the 1 less than the result of division and pass onto next iteration with the factorial value itself rather than the remainder (which would be 0)
* On reaching the final two positions, choose the second last character according to the remainder and leave the last character in the shuffled array
* Combine the unshuffled and the remnants of shuffled arrays and print the Nth lexicographic permutation


## Approach :-
1) **Store an array of characters of the word "abcdefghijklm" in $word$**
2) **Compute factorials from 1 to 13 and store them in an array $fact$**
3) **Starting from 1!, iterate incrementally over the factorials until the given required permutation number $n$ exceeds a factorial or otherwise till all factorials are traversed**
4) **Slice out the characters from 0 to $( - j - 2 )$ from $word$ as $unshuffle letters$ and remaining characters from $( - j - 1 )$ as $shuffle letters$**
5) **Assign permutation index variable $per index$ initially as $n$**
6) **While traversing decrementally over j as long as $( - j - 1 )$ remains less than 0, compute the $letter no$ for the $j$ th position by dividing $per index$ with $( j - 1 )$ th factorial**
7) **If $( j - 1 )$ th factorial divides $per index$ exactly, then append $unshuffle letters$ with $( letter no - 1 )$ th character from $shuffle letters$ and pop it out from $shuffle letters$. Also assign $per index$ as the $( j - 1 )$ th factorial itself**
8) **Otherwise append $unshuffle letters$ with $( letter no )$ th character from $shuffle letters$ and pop it out from $shuffle letters$. Assign $per index$ as the $per index$ (mod $( j - 1 )$ th factorial)**
9) **If $( j - 1 )$ th factorial reaches 1, then append $unshuffle letters$ with $( per index - 1 )$ th character from $shuffle letters$ and pop it out from $shuffle letters$**
10) **Join the $unshuffle letters$ list with the $shuffle letters$ which contains the last character left out after removal of other letters and print the $n$ th lexicographic permutation**

## Complexity :
**$O(t)$** (Each inner loop can only go upto maximum 13 iterations)
