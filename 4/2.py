def func(k):
    n = len(k)
    for i in range(1, n):
        j = i
        while j > 0 and k[j] < k[j-1]:
            k[j], k[j-1] = k[j-1], k[j]
            j -= 1
        print(' '.join(map(str, k)))
    return k

seq = input().split()
seq = list(map(int, seq))
func(seq)