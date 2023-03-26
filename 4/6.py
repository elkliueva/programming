def shell(step, k):
    for i in step:
        func(i, k)
        print(' '.join(map(str, k)))
    return k

def func(h, k):
    n = len(k)
    for i in range(h, n):
        j = i
        while j >= h and k[j] < k[j-h]:
            k[j], k[j-h] = k[j-h], k[j]
            j -= h
    return k

step = input().split()
step = list(map(int, step))
seq = input().split()
seq = list(map(int, seq))
shell(step, seq)