n = int(input())
last40 = first10 = 0
for i in range(n):
    nn = int(input())
    last40 += nn % (10 ** 40)
    first10 += nn // (10 ** 40)
print(((first10 + last40 // (10 ** 40))) //  10 ** (len(str(first10)) - 10))
