def func(k, exp):
    n = len(k)
    count = [0]*10
    output = [0]*n

    for i in range(n):
        index = k[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = k[i] // exp
        output[count[index % 10] - 1] = k[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        k[i] = output[i]


def sort(i, k):
    exp = 1
    for j in range(i):
        exp *= 10

    func(k, exp)

    for i in range(len(k)):
        k[i] = str(k[i])

    return ' '.join(k)


i = int(input())
k = list(map(int, input().split()))
print(sort(i, k))