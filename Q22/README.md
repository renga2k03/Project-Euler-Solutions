# Q22 - Names Scores

**Required Output :** Score for the given query where score of each name equals to the sum of its alphabets' positions (1-26) times the position of the name in a lexographically sorted list


## Idea :-
* Obtain the given list of names and sort it
* Use a dictionary/hashmap to store the scores for each name for efficient retrieval on being queried
* For each name, convert it into a list of characters and subtract 64 from their ascii values to obtain the numeric positions of the alphabets from A to Z aka 1 - 26
* Find the sum of all elements of the positions' array and compute its product with the index of the name in the sorted list
* Store the resultant value into the hashmap indexing with the name
* OBtain the number of queries and retrieve the appropriate scores for each name being queried


## Approach :-
1) **Store the names in a list $names$ and sort in ascending order**
2) **Iterate over the list of names and convert each of the names into a list of characters**
3) **Subtract each character's ascii value by 64 and store it in another list $namechars$**
4) **Compute the sum of values in $namechars$ and multiply with the index of the name in the list $( i + 1 )$**
5) **Store the resultant value in a dictionary $score$ indexed with the name itself**
6) **Get the number of queries and for each name being queried, print the score mapped in the dictionary**

## Complexity :
**$O(n * log n)$** (Sorting the list takes more time than the traversal over queries as well as computing the scores for each names since each name doesn't exceed length of 12 as per test case constraints)
