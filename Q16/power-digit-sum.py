t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int, list(str(2**n))))
    print(sum(num))
