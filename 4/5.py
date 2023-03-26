def func(h, k):
    n = len(k)
    for i in range(h, n):
        j = i
        while j >= h and k[j] < k[j-h]:
            k[j], k[j-h] = k[j-h], k[j]
            j -= h
        print(' '.join(map(str, k)))
    return k
   


h = int(input())
seq = input().split()
seq = list(map(int, seq))
func(h, seq)