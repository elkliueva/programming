def func(k):
    n = len(k)
    for i in range(n-1):
        index = i
        for j in range(i+1, n):
            if k[j] < k[index]:
                index = j
        k[i], k[index] = k[index], k[i]
        print(' '.join(map(str, k)))
    return k
        

seq = input().split()
seq = list(map(int, seq))
func(seq)