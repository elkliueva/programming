def func(k):
    n = len(k)
    for i in range(n-1):
        for j in range(n-i-1):
            if k[j] > k[j+1]:
                k[j], k[j+1] = k[j+1], k[j]
        print(' '.join(map(str, k)))
    return k

seq = input().split()
seq = list(map(int, seq))
func(seq)