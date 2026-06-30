# Q24 - Lexicographic Permutations

**Required Output :** Nth lexicographic permutation of the word "abcdefghijklm"


## Idea :-
* Computing and iterating through all permutations of the given word can be tedious and cause TLE due to huge number of iterations and even the memory space required to store them which could go up to 13!
* As the word is already given to be "abcdefghijklm", store the characters of the word in an array and also all factorials upto 13 in another array
* Each factorial from 1 to 13 indicates the number of shuffles or permutations possible in characters from 1 to 13 positions respectively
* To identify the number of characters to be shuffled for the given position N, find the smallest factorial that exceeds the given number
* Seperate the entire word into two arrays, one for the unshuffled characters with respect to the test case and other for the shuffled characters which comprises the entities from the position where the factorial exceeds the given number
* From left to right in the shuffled array, the number of possible letters in each position would decreases from being possible to place any letters in the lefmost position to being able to place only the remaining one character in the rightmost position
* To find out the shuffle step count of each position, divide the given position N with the factorial of each position's permutation count to find the step count of shuffle and append the letter to the unshuffled list while popping it out from the shuffled list.
* Also proceed to the next position with the remainder when N is divided by the factorial of that position
* But if the factorial exactly divides N, then consider the shuffle step count to be the 1 less than the result of division and pass onto next iteration with the factorial value itself rather than the remainder
* On reaching the final two positions, choose the second last character according to the remainder and leave the last character in the shuffled array
* Combine the unshuffled and the remnants of shuffled arrays and print the Nth lexicographic permutation


## Approach :-
1) **Store an array of characters of the word "abcdefghijklm" in $word$**
2) **Compute factorials from 1 to 13 and store them in an array $fact$**
3) **Starting from 1!, iterate incrementally over the factorials until the given required permutation number $n$ exceeds a factorial and otherwise till all factorials are traversed**
4) **Slice out the characters from 0 to $( - j - 2 )$ from $word$ as $unshuffle_letters$ and remaining characters from $( - j - 1 )$ as $shuffle_letters$**
5) **Assign permutation index variable $per_index$ initially as $n$**
6) **While traversing decrementally over j as long as $( - j - 1 )$ remains less than 0, compute the $letter_no$ for the $j$th position by dividing $per_index$ with $( j - 1 )$th factorial**
7) **If $( j - 1 )$th factorial divides $per_index$ exactly, then append $unshuffle_letters$ with $( letter_no - 1 )$th character from $shuffle_letters$ and pop it out from $shuffle_letters$. Also assign $per_index$ as the $( j - 1 )$th factorial itself**
8) **Otherwise append $unshuffle_letters$ with $( letter_no )$th character from $shuffle_letters$ and pop it out from $shuffle_letters$. Assign $per_index$ as the $per_index$ (mod $( j - 1 )$th factorial)**
9) **If $( j - 1 )$th factorial reaches 1, then append $unshuffle_letters$ with $( per_index - 1 )$th character from $shuffle_letters$ and pop it out from $shuffle_letters$**
10) **Join the $unshuffle_letters$ list with the $shuffle_letters$ which contains the last character left out after removal of other letters and print the $n$th lexicographic permutation

## Complexity :
**$O(t)$** (Each inner loop can only go upto maximum 13 iterations)
