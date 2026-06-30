t = int(input())
word = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
fact = []
f = 1
for i in range(1, 14):
    f *= i
    fact.append(f)
for i in range(t):
    n = int(input())
    j = 0
    while fact[j] < n and j < 13:
        j += 1
    unshuffle_letters = word[:-j-1]
    shuffle_letters = word[-j-1:]
    per_index = n
    while (-j-1) < 0:
        if fact[j-1] == 1:
            unshuffle_letters += shuffle_letters[per_index-1]
            shuffle_letters.pop(per_index-1)
            break
        letter_no = per_index // fact[j-1]
        if per_index % fact[j-1] == 0:
            unshuffle_letters += shuffle_letters[letter_no-1]
            shuffle_letters.pop(letter_no-1)
            per_index = fact[j-1]
        else:
            unshuffle_letters += shuffle_letters[letter_no]
            shuffle_letters.pop(letter_no)
            per_index = per_index % fact[j-1]
        j -= 1
    print(''.join(unshuffle_letters + shuffle_letters))
