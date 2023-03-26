def func(k):
    count = [0] * 1001
    sorted_k = [0] * len(k)
    for num in k:
        count[num] += 1
    for i in range(1, 1001):
        count[i] += count[i-1]
    for num in k[::-1]:
        sorted_k[count[num]-1] = num
        count[num] -= 1
    return ' '.join(map(str, sorted_k))

seq = input().split()
seq = list(map(int, seq))
print(func(seq))


