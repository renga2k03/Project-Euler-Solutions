n = int(input())
names = []
for i in range(n):
    names.append(input())
names.sort()
score = {}
for i in range(n):
    namechars = [ord(ch) - 64 for ch in list(names[i])]
    score[names[i]] = sum(namechars) * (i + 1)
q = int(input())
for i in range(q):
    print(score[input()])
